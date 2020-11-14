# templatetags for sidebar


from django import template

# Будем выводит последние посты(популярные) и облако тего
from blog.models import  Post,Tag

register=template.Library()
@register.inclusion_tag('blog/popular_posts_tpl.html')
# в качестве параметра будет количество
# постов которые нужно выводить
def get_popular(cnt=3):
    # чтобы получить популрыне посты ,
    # мы должны их отсортировать по просмотру
    # в обратно порядке
    posts=Post.objects.order_by('-views')[:cnt]
    return {'posts':posts}


@register.inclusion_tag('blog/tags_posts_tpl.html')
def get_tags():
    # выводим теги
    tags=Tag.objects.all()
    return {'tags':tags}




