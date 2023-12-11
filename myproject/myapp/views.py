from django.shortcuts import render
from .models import MyModel


# получение всех записей
def home(request):
    return render(request, 'myapp/home.html', {'categories': MyModel.objects.all()})


