from django.shortcuts import render
from django.urls import reverse

from .models import Rubric
# Create your views here.

def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass


 def get_absolute_url(self):
        return reverse('rubric',kwargs={"pk":self.pk})