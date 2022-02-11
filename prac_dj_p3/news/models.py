from django.db import models

# Create your models here.
class Articles(models.Model):

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Краткое описание', max_length=200)
    full_text = models.TextField('Статья', max_length=5000)
    date = models.DateTimeField('Время создания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):#   в методе указывается страница на которую нужно переадресовывать 
        return f'/news/{self.id}'# пользователя, после того как мы обновим или удалим статью