from django.http import HttpResponse
from django.shortcuts import render

import datetime

def hello(request):
    context = {}
    context["hello"] = "hello world!"
    test_dict = {"name": "Mysite"}
    now_time = datetime.datetime.now()
    # return HttpResponse("hello world!")

    # return render(request, "index.html", {"name": test_dict})
    return render(request, "index.html", {"4.time": now_time})




