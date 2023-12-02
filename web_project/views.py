from django.http import HttpResponse
from django.shortcuts import render

data = {
    "reasons_to_learn": [
        {"reason": "Clean design"},
        {"reason": "Python power"},
        {"reason": "Community"},
        {"reason": "Django is fun"},
    ],
}


def home(request):
    return HttpResponse("Hello, Django!")


def about(request):
    return render(request, "web_project/about.html", data)

def contact(request):
    return render(request, "web_project/contact.html", "hello world")