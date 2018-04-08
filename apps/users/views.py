from django.shortcuts import render, HttpResponse, redirect
from .models import User 
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "user": User.objects.all()
    }
    return render(request,'users/users_index.html', context)

def click_add_new_user(request):

    return render(request, "users/users_new.html")

def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors): 
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
        else:

            User.objects.create(name=request.POST['name'], email=request.POST['email'])
    


            return redirect('/users')
    # return redirect('/users/new')
def go_back(request):

    return redirect("/users")

def show(request, id):
    idk ={
        "user": User.objects.get(id=id)
    }
    
    return render(request,'users/users_show.html', idk)

def edit(request, id):
    
    idgf={
        "user":User.objects.get(id=id)
    }

    return render(request,'users/users_edit.html', idgf) 
    
def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors): 
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/users/"+id+"/edit")
    else:
        e = User.objects.get(id=id)
        e.name = request.POST['name']
        e.email = request.POST['email']
        e.save()

        return redirect("/users")

def destory(request, id):
    d=User.objects.get(id=id)
    d.delete()
    return redirect("/users")


    