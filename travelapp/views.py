from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import blog
# Create your views here.
def fun(request):
    object=place.objects.all()
    objec = blog.objects.all()
    return render(request, "index.html",{'results':object,'vlogs':objec})




