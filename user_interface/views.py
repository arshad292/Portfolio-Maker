from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from . models import *
from . forms import *
# Create your views here.

def index(request):
    return render(request, template_name="user_interface/index.html")
    # return HttpResponse("Hello")
    

#create, retrieve, update, delete
def form_createView(request, *args, **kwargs):
    template_name = 'user_interface/create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        user = "admin"
        
    intro_form = IntroForm(request.POST or None)
    if intro_form.is_valid():
        intro_form.save(commit=False)
        intro_form.user = user
        intro_form.save(request = request)
    else:
        intro_form = IntroForm()
        
    edu_form = EducationForm(request.POST or None)
    if edu_form.is_valid():
        edu_form.save(commit=False)
        edu_form.user = user
        edu_form.save(request = request)
    else:
        edu_form = EducationForm()
        
    exp_form = ExperienceForm(request.POST or None)
    if exp_form.is_valid():
        exp_form.save(commit=False)
        exp_form.user = user
        exp_form.save(request = request)
    else:
        exp_form = ExperienceForm()
        
    project_form = ProjectForm(request.POST or None)
    if project_form.is_valid():
        project_form.save(commit=False)
        project_form.user = user
        project_form.save(request = request)
    else:
        project_form = ProjectForm()
        
    skill_form = SkillsetForm(request.POST or None)
    if skill_form.is_valid():
        skill_form.save(commit=False)
        skill_form.user = user
        skill_form.save(request = request)
    else:
        skill_form = SkillsetForm()
        
    context = {
        'user' : user,
        'introFORM' : IntroForm(),
        'eduFORM' : EducationForm(),
        'expFORM' : ExperienceForm(),
        'projectFORM' : ProjectForm(),
        'skillFORM' : SkillsetForm(),
    }
    
    return render(request, template_name, context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def login_view(request,*args, **kwargs):
    if request.method == "POST":
        
        #attempt the user to sign in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        #check if authentication is successfull
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("information"))
        else:
            return render(request, "user_interface/loginRegister.html", {"message": "invalid user or password. Please check again"})
    else:
        return render(request, "user_interface/loginRegister.html", {"message": ""})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
    
def register_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        #ensure password matches the confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password !=  confirmation:
            return render(request, "user_interface/loginRegister.html", {"message": "Password not confirmed/matching. Please enter again"})
        
        #attempt to create new user
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "user_interface/loginRegister.html", {"message": "Username already exists. "})
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "user_interface/loginRegister.html")
        