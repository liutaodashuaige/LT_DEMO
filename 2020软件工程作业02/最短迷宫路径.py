#coding:utf-8
def get_data():#获取用户输入的地图阶数和地图数据
    n = int(input())
    min_step = n * n
    my_list = [[0] * n] * n
    for i in range(n):
        my_list[i] = input().split(" ")
        my_list[i] = list(map(int, my_list[i]))
    return my_list, min_step, n

def path_find(point_x, point_y, count, n):#通过递归得到最短路径所需步数
    global Min_step, My_list
    if point_x == n-2 and point_y == n-2:#到达终点
        Min_step = min(count, Min_step)#得到当前最短路径步数
    else:
        My_list[point_x][point_y] = 1#不可以重复走同一个位置
        if point_y < n-1 and My_list[point_x][point_y + 1] == 0:#向右
            path_find(point_x, point_y + 1, count + 1, n)
        if point_x < n-1 and My_list[point_x + 1][point_y] == 0:#向下
            path_find(point_x + 1, point_y, count + 1, n)
        if point_y > 1 and My_list[point_x][point_y - 1] == 0:#向上
            path_find(point_x, point_y - 1, count + 1, n)
        if point_x > 1 and My_list[point_x - 1][point_y] == 0:#向左
            path_find(point_x - 1, point_y, count + 1, n)
        #回溯:当路线无法到达终点时，依次重置路过的位置
        My_list[point_x][point_y] = 0

if __name__ == '__main__':
    My_list, Min_step, n = get_data()
    path_find(1, 1, 0, n)
    if Min_step == n*n:
        print('No solution')
    else:
        print('最短步长为', Min_step)
