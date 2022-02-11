from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

# 10 урок. Импортируем DetailView, для создания своего класса на основании предустановленного 
# На основании этого мы создадим динамическую страницу
class UserNewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'# Какой шаблон будет обрабатывать эту динамическую страницу
    context_object_name = 'article'# наименование ключа по которому мы будем передавать саму определенную запись внутрь шаблона


# https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#updateview
class UserNewsEditView(UpdateView):
    model = Articles
    template_name = 'news/create.html'# Берем create, т.к. у нас в ее форму есть поля которые можно заполнить
    #fields = ['title','anons','full_text','date']
    form_class = ArticlesForm# Мы наследуем из формы, т.к. там уже всё красиво


class UserNewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'
    context_object_name = 'article'


# до 10 урока
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news} ) 

def create_news(request):
    error = ''
    # получение данных из формы, проверку, и занесение либо вывод уведомления
    if request.method == 'POST':# мы сами указали в create.html метод пост
        form = ArticlesForm(request.POST)# данные пользователя из формы
        if form.is_valid():# данный метод находится в ModelsForm
            form.save()
            return redirect('news_home')
        else:
            error = 'форма была неверная'
    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)