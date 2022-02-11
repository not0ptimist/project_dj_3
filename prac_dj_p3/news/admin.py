from django.contrib import admin
from .models import Articles

# Register your models here.
#admin.site.register(Articles)

@admin.register(Articles)
class PageAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ['title', 'anons', 'date']
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
    # не перепутать с **eld , который автоматом не заполняет при заполнении указанного поля title
    # prepopulated_fields = {"slug": ("title",)}