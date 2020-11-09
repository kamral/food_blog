from django.db import models

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
        ordering=['title']

class Tag(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название категории', )
    slug = models.SlugField(max_length=255,
                            verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
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


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']




