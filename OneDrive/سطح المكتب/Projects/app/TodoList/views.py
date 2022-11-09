from django.shortcuts import render, redirect
from .models import Base

def Home(request):
    todo_list = Base.objects.all()
    if request.method == 'POST':
        new_todolist = Base(task = request.POST['title'])
        new_todolist.save()
        return redirect('Home')

    return render(request, 'home.html', {'todos': todo_list})

def Delete(request, pk):
    todo_list = Base.objects.get(id=pk)
    todo_list.delete()
    return redirect('Home')

def Done(request, pk):
    todo_list = Base.objects.get(id=pk)
    todo_list.completed= True
    todo_list.save()
    return redirect('Home')

def Active(request, pk):
    todo_list = Base.objects.get(id=pk)
    todo_list.completed= False
    todo_list.save()
    return redirect('Home')

