from django.shortcuts import render, redirect
from .models import Base

# Create your views here.
def home(request):
    todo_list = Base.objects.all()
    if request.method == 'POST':
        new_todolist = Base(task = request.POST['title'])
        new_todolist.save()
        return redirect('/')

    return render(request, 'home.html', {'todos': todo_list})

def done(request, pk):
    todo_list = Base.objects.get(id=pk)
    todo_list.delete()
    return redirect('/')