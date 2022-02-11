from django.shortcuts import render

# Create your views here.


# def index(request):
#     return render(request, 'blog/layout.html')#самый детский файл, а не тот дед который на виду

def index(request):
    data = {
        'title': 'Главная страница.', # Далее идут ненужные данные
        'values': ['Some', 'Hello', '123'],
        'objects': {
            'car': 'Volvo',
            'age': '20',
            'hobby': 'Rally'
        }
    }
    return render(request, 'blog/layout.html', data) 

def about(request):
    return render(request, 'blog/about.html')