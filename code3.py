## 图书管理
def menu():
    # 显示主菜单
    print('\n' + '-' * 10 + '图书订单管理' + '-' * 10)
    print(' 请选择您的操作:')
    print(' 1----订单查询')  # cx()
    print(' 2----订单更新')  # gx()
    print(' 3----订单删除')  # sc()
    print(' 4----订单增加')  # zj()
    print(' 5----订单结构修改')  # xg()
    print(' 6----订单排序')  # px()
    print(' 0----结束')
    print('*' * 30)


def cx():  # 订单查询
    print('你选择的是订单查询')
    bookname = input()
    path = '/data/workspace/myshixun/datafile/orders.txt'
    orderno = 0
    booknum = 0
    fr = open(path, 'r', encoding='gbk')
    # txt = fr.readlines()
    for row in fr:
        line = row.split(',')
        if bookname == line[1]:
            print(row)
            orderno += 1
            booknum += int(line[-1])
            price = line[2]
    if booknum > 0:
        total = booknum * eval(price)
        print('{}的订单数是{},共{}本{}元'.format(bookname, orderno, booknum, total))
    else:
        print('无此书订单')

#波音0115汪琰的代码文件
def gx():  # 订单更新-更新图书名称
    print('你选择的是订单更新')
    ## 补充代码开始  ##
    bookno = input()
    bookname = input()

    path1 = '/data/workspace/myshixun/datafile/orders.txt'
    path2 = '/data/workspace/myshixun/datafile/update.txt'
    fold = open(path1, 'r', encoding='gbk')
    lines = []
    for row in fold:
        line = row.split(',')
        if bookno == line[0]:
            line[1] = bookname
        p = ','.join(line)
        lines.append(p)
    s = '\n'.join(lines)
    # print(s)
    fnew = open(path2, 'w+')
    fnew.write(s)
    fnew.close()
    ## 补充代码结束  ##
    #下面这部分有改动
    fr = open(path2, 'r')
    cnt = 0
    for row in fr:
        # print(row)
        line = row.split(',')
        if len(line) == 4 and bookname == line[1]:
            print(row)
            cnt = cnt + 1
    if cnt == 0:
        print('无此书订单')


def sc():  # 订单删除
    print('你选择的是订单删除')


def zj():  # 订单增加
    print('你选择的是订单增加')


def xg():  # 订单结构修改-增加金额项
    print('你选择的是订单结构修改')


def px():  # 订单排序
    print('你选择的是订单排序')


# main
def main():
    menu()  # 显示菜单
    choice = int(input('请选择任务(输入0结束程序)：'))
    while choice != 0:
        if choice == 1:
            cx()
        elif choice == 2:
            gx()
        elif choice == 3:
            sc()
        elif choice == 4:
            zj()
        elif choice == 5:
            xg()
        elif choice == 6:
            px()
        else:
            print('输入错误，请重新输入你的选择，输入0结束程序：')
        menu()
        choice = int(input())
    print('退出图书订单管理程序')


## 调用主函数
main()
