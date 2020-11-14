# данный файл предназначен для создания меню

from django import template
# так как мы строим менб для категории ,
# импортируем соответ-ую модель

from blog.models import  Category

register=template.Library()

# написали декоратор который будет
# декорировать нашу функцию showmenu
@register.inclusion_tag('blog/menu_tpl.html')
# мы передаем в параметре класс меню из _header.html
def show_menu(menu_class='menu'):
    # необходимо получить категорию
    categories=Category.objects.all()
    # и возвращаем их ввиде словаря
    return {'categories':categories,'menu_class':menu_class}

# осталось дописать логику работы шаблона menu_tpl.html
