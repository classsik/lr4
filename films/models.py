from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название фильма')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    release_date = models.DateField(verbose_name='Дата выпуска')
    actors = models.TextField(verbose_name='Актеры')
    show_date = models.DateField(verbose_name='Дата показа')

    def __str__(self):
        return self.name

