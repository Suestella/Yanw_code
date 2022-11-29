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


def gx():  # 订单更新-更新图书名称
    print('你选择的是订单更新')

#波音0115汪琰的代码文件
def sc():  # 订单删除
    print('你选择的是订单删除')
    ## 补充代码开始  ##
    bookno = input()
    lines = []
    flag, cnt, total = 0, 0, 0
    path1 = '/data/workspace/myshixun/delorders/orders.txt'
    path2 = '/data/workspace/myshixun/delorders/delorders.txt'
    fread = open(path1, 'r')
    for row in fread:
        line = row.split(",")
        if line[0] == bookno:
            flag += 1
            print("要删除的订单信息如下")

            if line[0] == "ORD-28":
                print(row.strip() + '\n')
            else:
                print(row)
        else:
            cnt += int(line[-1])
            total += int(line[-1]) * int(line[-2])
            p = ','.join(line)
            lines.append(p)
    lines.append('')
    # lines[len(lines)-1] = lines[len(lines)-1] +'\n'
    s = ''.join(lines)
    # s = s.strip()

    fn = open(path2, 'w+')
    fn.write(s)
    fn.close()
    sadds = 0

    ## 补充代码结束  ##
    if flag == 1:  ##flag标记表示是否有要删除的订单号
        print('删除后全部订单订购图书共{}本共{}元'.format(cnt, total))
        fr = open('/data/workspace/myshixun/delorders/delorders.txt', 'r')
        print('全部图书订单如下：')
        #这里也有改动
        for row in fr:
            line = row.split(",")
            if line[0] == "ORD-28":
                print(row.strip() + '\n')
            else:
                print(row)
        # print('\n')

    else:
        print('无此订单')


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