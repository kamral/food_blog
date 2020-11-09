from django.db import models
from PIL import Image
# Create your models here.


'''
Category
title,slug
____________

Tag
title,slug
_____________

Post
title, content, 
created_at,photo,views,category,tags
author
___________

'''


class Category(models.Model):
    title=models.CharField(max_length=255,
                           verbose_name='Название категории',)
    slug=models.SlugField(max_length=255,
                          verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']

class Tag(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название категории', )
    slug = models.SlugField(max_length=255,
                            verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,
                                    verbose_name='Оубликованно')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    views=models.IntegerField(default=0,verbose_name='Количество просомтров')
    category=models.ForeignKey(Category,on_delete=models.PROTECT,
                               related_name='posts')
    tag=models.ManyToManyField(Tag,blank=True,related_name='posts')



    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        # Выбор картинки
        img = Image.open(self.cover.path)
        # Условие
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover.path)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']




