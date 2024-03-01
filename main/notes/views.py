from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    context = {'page':'Home Page'}
    return render(request, 'homepage.html',context)

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/notes/')
        
    context = {'page':'Login Page'} 
    return render(request,'login.html',context)

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create (
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.error(request, 'Account created Successfully')
        return redirect('/register/')
    context = {'page':'Register'}  
    return render(request,'signup.html',context)
def logout_page(request):
    logout(request)
    return redirect('/login/')
@login_required(login_url="/login/")
def notes(request):
    if request.method == "POST":
        data = request.POST
        note_name = data.get('note_name')
        note_description = data.get('note_description')

        Notes.objects.create(
            note_name = note_name,
            note_description = note_description,
        )
        return redirect('/notes/')
    
    queryset = Notes.objects.all()
    context = {"notes": queryset}
    return render(request,'writenotes.html',context)

def delete_note(request , id):
    queryset = Notes.objects.get(id = id)
    queryset.delete()
    return redirect('/view_notes/')

def update_note(request,id):
    queryset = Notes.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        note_name = data.get('note_name')
        note_description = data.get('note_description')

        queryset.note_name = note_name
        queryset.note_description = note_description
        queryset.save()
        return redirect('/notes/')
    context = {"notes": queryset}
    return render (request,'update.html',context)

def view_notes(request):
    queryset = Notes.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(note_name__icontains = request.GET.get('search'))
    context = {"notes": queryset}
    return render (request,'view_notes.html',context)

