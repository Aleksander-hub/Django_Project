# news/models.py
from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=50)
    full_text = models.TextField('Статья', max_length=100)
    date = models.DateTimeField('Дата публикации')
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    # ... другие поля ...

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
