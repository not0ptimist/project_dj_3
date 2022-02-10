from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/layout.html')#самый детский файл, а не тот дед который на виду

def about(request):
    return render(request, 'blog/about.html')