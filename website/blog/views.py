import random

from django.shortcuts import render


def dummy():
    return str(random.randint(1, 10))


# Create your views here.
def index(request):
    title = "My blog"
    lst = ["one", "two", "three"]
    dict = {
        "title": title,
        "func": dummy,
        "lst": lst
    }
    return render(request, "blog/index.html", context=dict)

def post(request):
    return render(request, "blog/post.html")


def about(request):
    return render(request, "blog/about.html")


def services(request):
    return render(request, "blog/services.html")


def contact(request):
    return render(request, "blog/contact.html")

