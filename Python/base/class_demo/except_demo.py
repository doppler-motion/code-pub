import traceback

# def main():
#     try:
#         # 使用try...except来捕捉异常
#         # 此时即使程序出现异常，也不会传播给main函数
#         mtd(3)
#     except Exception as e:
#         print('程序出现异常:', e)
#         #        help(e.with_traceback)
#         traceback.print_exc()
#     #        e.with_traceback(e)
#     # 不使用try...except捕捉异常，异常会传播出来导致程序中止
#     mtd(3)
#
#
# def mtd(a):
#     if a > 0:
#         raise ValueError("a的值大于0，不符合要求")
#
#
# main()


# def foo():
#     try:
#         fis = open("a.txt");
#     except Exception as e:
#         # 访问异常的错误编号和详细信息
#         print(e.args)
#         # 访问异常的错误编号
#         print(e.errno)
#         # 访问异常的详细信息
#         print(e.strerror)
#
#
# foo()

# class AuctionException(Exception): pass
#
#
# class AuctionTest:
#     def __init__(self, init_price):
#         self.init_price = init_price
#
#     def bid(self, bid_price):
#         d = 0.0
#         try:
#             d = float(bid_price)
#         except Exception as e:
#             # 此处只是简单地打印异常信息
#             print("转换出异常：", e)
#             # 再次引发自定义异常
#             #            raise AuctionException("竞拍价必须是数值，不能包含其他字符！")  # ①
#             raise AuctionException(e)
#         if self.init_price > d:
#             raise AuctionException("竞拍价比起拍价低，不允许竞拍！")
#         initPrice = d
#
#
# def main():
#     at = AuctionTest(20.4)
#     try:
#         at.bid("df")
#     except AuctionException as ae:
#         # 再次捕获到bid()方法中的异常，并对该异常进行处理
#         print('main函数捕捉的异常：', ae)
#
#
# main()

# 导入trackback模块
import traceback


class SelfException(Exception): pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


try:
    main()
except:
    # 捕捉异常，并将异常传播信息输出控制台
    traceback.print_exc()
    # 捕捉异常，并将异常传播信息输出指定文件中
    traceback.print_exc(file=open('log.txt', 'a'))

# class SelfException(Exception): pass
#
#
# def main():
#     firstMethod()
#
#
# def firstMethod():
#     secondMethod()
#
#
# def secondMethod():
#     thirdMethod()
#
#
# def thirdMethod():
#     print(1)
#     # raise Exception("自定义异常信息")
#
#
# main()
