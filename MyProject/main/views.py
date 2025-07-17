from django.shortcuts import redirect, render
from .models import *
from django.views.generic import ListView, DetailView
from .forms import MessageModelForm,CreateUserForm
from django.contrib.auth import login,logout,authenticate

class HomeListView(ListView):
    template_name='index.html'
    
    def get(self,request):
        form=MessageModelForm()

        context={
            'form':form
        }

        return render(request,self.template_name,context)
    
    def post(self,request):
        error=''
        form=MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error=form.errors
        context={
            'form':form,
            'error':error
        }

        return render(request,self.template_name,context)
        
    

def RegisterPage(request):
    message = None  
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            message = form.errors
    else:
        form = CreateUserForm()  

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'register.html', context)

def LoginPage(request):
    message=None
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message='username or password in valid'
    
    return render(request,'login.html',{'message':message})

def LogoutPage(request):
    logout(request)
    return redirect('home')

