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

#波音0115汪琰的代码文件
def cx():  # 订单查询
    print('你选择的是订单查询')
    pass


def gx():  # 订单更新-更新图书名称
    print('你选择的是订单更新')


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
    ## 补充代码开始  ##

    while True:
        menu()
        # print("请选择任务(输入0结束程序)：",end="")
        x = eval(input())
        if x == 1:
            print("请选择任务(输入0结束程序)：", end="")
            cx()
        elif x == 2:
            print("请选择任务(输入0结束程序)：", end="")
            gx()
        elif x == 3:
            print("请选择任务(输入0结束程序)：", end="")
            sc()
        elif x == 4:
            print("请选择任务(输入0结束程序)：", end="")
            zj()
        elif x == 5:
            print("请选择任务(输入0结束程序)：", end="")
            xg()
        elif x == 6:
            print("请选择任务(输入0结束程序)：", end="")
            px()
        elif x == 0:
            print("退出图书订单管理程序")
            break
        else:
            print("输入错误，请重新输入你的选择，输入0结束程序：")

    ## 补充代码结束  ##


## 调用主函数
main()