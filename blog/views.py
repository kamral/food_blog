from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post,Category,Tag
from django.db.models import F

class Home(ListView):
    model=Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        # вызовим родительский метод
        context=super().get_context_data(**kwargs)
        context['title']='CLASSIC BLOG DESIGN'
        return context

# позволяет каждой записи быть относенной к каждой категории в меню
class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    # чтобы при запросе пустой категории было 404 ответ, а не 500

    def get_context_data(self, *, object_list=None, **kwargs):
        # вызовим родительский метод
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])




class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        # вызовим родительский метод
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class PostByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    # чтобы при запросе пустой категории было 404 ответ, а не 500
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        # вызовим родительский метод
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: '+str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context