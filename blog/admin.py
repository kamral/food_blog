from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}

class TagAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)