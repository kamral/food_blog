from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}
    forms=PostAdminForm
    save_on_top = True
    list_display = ('id','title','slug','category',
                    'created_at','get_photo','views')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('category','tag')
    readonly_fields = ('views','created_at', 'get_photo')
    fields = ('title','slug','content','category','tag','views',
                    'created_at','photo','author')

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        else:
            return '--'

    get_photo.short_description = 'photo'

class CategoryAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}

class TagAdmin(admin.ModelAdmin):
    # на основе title будем формировать slug
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)