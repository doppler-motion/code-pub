from django.shortcuts import render, HttpResponse

from . import models

def add_book(request):
    book = models.Book(title="菜鸟学Python", price=300, publish="匿名出版社", pub_date="2008-8-8")
    book.save()
    return HttpResponse("<p> 数据添加成功！</p>")


def check_book(request):
    books = models.Book.objects.all()
    print(books, type(books))
    return HttpResponse("<p> 查询成功 </p>")

