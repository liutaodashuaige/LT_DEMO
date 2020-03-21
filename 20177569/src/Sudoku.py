# -*- coding: UTF-8 -*-
import sys
import getopt
#全局变量
M = ""
N = ""
MY_MAPS = []
op = ""

def judge(_i_, _x_, _y_):
    """
    合法性判断
    :return:
    """
    global M,MY_MAPS
    #行列不重复判断
    for i in range(M):
        if i != _x_ and MY_MAPS[_i_][_x_][_y_] == MY_MAPS[_i_][i][_y_]:
            return 0
        if i != _y_ and MY_MAPS[_i_][_x_][_y_] == MY_MAPS[_i_][_x_][i]:
            return 0
    #区块重复判断
    x1 = y1 = row = col = 0#块内坐标初始值
    #区块定位参考于https://github.com/zxw0621/demo/blob/master/20177596/src/sudoku.py#L42
    #这定位写的太好了
    #根据其阶数确定其模块规模以及所属模块
    if M % 3 == 0:
        row = 3
        col = int(M / 3)
    elif M % 2 == 0:
        row = 2
        col = int(M / 2)
    x1 = int(_x_ // row * row)
    y1 = int(_y_ // col * col)
    #遍历所属区块，检查其合法性
    for i in range(x1, x1 + row):
        for j in range(y1, y1 + col):
            if _x_ != i and _y_ != j and MY_MAPS[_i_][_x_][_y_] == MY_MAPS[_i_][i][j]:
                return 0
    return 1

def DFS(_i_, _x_, _y_):
    """
    【DFS】深度优先搜索递归方式
    :return:
    """
    #声明引用全局变量
    global M,MY_MAPS
    if _x_ > M - 1:#完成条件
        MY_OTP(_i_)#保存数值
    elif MY_MAPS[_i_][_x_][_y_] != 0:#当前格子不可填
        if _y_ == M - 1:#右边界换行
            DFS(_i_, _x_ + 1, 0)
        else:
            DFS(_i_, _x_, _y_ + 1)#下一格
    else:#当前格可填
        for i in range(1, M + 1):
            MY_MAPS[_i_][_x_][_y_] = i #试探填入数值
            if judge(_i_, _x_, _y_): #判断其试探值的合法性,当判断函数返回值为1即合法
                if _y_ == M - 1: #边界情况
                    DFS(_i_, _x_ + 1, 0)
                else:
                    DFS(_i_, _x_, _y_ + 1)
            #回溯
            MY_MAPS[_i_][_x_][_y_] = 0

def MY_OTP(_i_):
    """
    向文件内写入所得矩阵
    :return:
    """
    global N,M,MY_MAPS,op
    #遍历当前求解矩阵
    for x in range(M):
        for y in range(M):
            op.write(str(MY_MAPS[_i_][x][y]) + ' ')
        op.write('\n')#换行


def main(argv):
    """
    通过sys模块来识别参数
    :return:
    """
    #声明全局变量
    global M,N
    global MY_MAPS,op
    in_put = ""
    out_put = ""
    try:#获取参数并处理异常
        opts, args = getopt.getopt(argv, "m:n:i:o:", ["help"])
    except getopt.GetoptError:
        print('Error: Sudoku.py -m -n -i -o')
        sys.exit(2)
    #处理获取的参数
    for opt, arg in opts:
        if opt in ("--help"):#给予帮助提示
            print('Error: Sudoku.py -m -n -i -o')
            sys.exit()
        elif opt in ("-m"):
            M = int(arg)
        elif opt in ("-n"):
            N = int(arg)
        elif opt in ("-i"):
            in_put = arg
        elif opt in ("-o"):
            out_put = arg
    with open(in_put,'r',encoding='utf-8') as fp:#以读状态打开指定文件读取矩阵
        MY_MAP = []
        for line in fp.readlines():
            if line != '\n':#用换行符分割矩阵
                MY_MAP.append(list(map(int, line.strip().split(" "))))
            else:
                MY_MAPS.append(MY_MAP)
                MY_MAP = []
        MY_MAPS.append(MY_MAP)#MY_MAPS是集合了所有数据的三维数组

    op = open(out_put,'w', encoding='utf-8')

    for i in range(N):
         if i > 0:
             op.write('\n')#分割矩阵
         DFS(i, 0, 0)#递归求解
    op.close()



if __name__ == '__main__':
    #sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，因此弃之不用
    main(sys.argv[1:])
