from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Classes, Subjects,subtopic,Topics,image
def home(request):
    return render(request,'home.html')
def subject_redirecting(request):
    return redirect('subjects')
def courses(request):
    Subject=Subjects.objects.all()
    return render(request,'Subjects.html',{'subjects':Subject,'image':image})
def topic(request,sub):
    topics=Topics.objects.filter(Subject__Subject=sub)
    topic_sub={}
    for topicc in topics:
        topic_sub[topicc]=subtopic.objects.filter(Topic__Topic=topicc)
    return render(request,'topic.html',{'topic_sub':topic_sub,'sub':sub})
def subtopics(request,pk):
    Current_Subtopic=subtopic.objects.get(id=pk)
    Subtopics_of_topic=subtopic.objects.filter(Topic__Topic=Current_Subtopic.Topic.Topic).order_by("id")
    return render(request,'subtopic.html',{'subtopic':Current_Subtopic,'subtopics_of_topic':Subtopics_of_topic})
def nextpage(request,pk,sometext):
    current_subtopic=subtopic.objects.get(id=pk)
    if subtopic.objects.filter(id__gt=pk).exists():
        next_subtopic=subtopic.objects.filter(Subject__Subject=current_subtopic.Subject.Subject,id__gt=pk).order_by('id').first()
        return redirect('subtopic',pk=next_subtopic.id)
    else:
        return redirect('subtopic',pk=current_subtopic.id)
def previouspage(request,pk,somestring):
    current_subtopic=subtopic.objects.get(id=pk)
    if subtopic.objects.filter(Subject__Subject=current_subtopic.Subject.Subject,id__lt=pk).exists():
        previous_subtopics=subtopic.objects.filter(Subject__Subject=current_subtopic.Subject.Subject,id__lt=pk).order_by('-id').first()
        return redirect('subtopic',pk=previous_subtopics.id)
    else:
        return redirect('subtopic',pk=current_subtopic.id)
def sidebar(request,pk,something):
    return redirect('subtopic',pk=pk)
def signup(request):
    if request.method=='POST':
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                return redirect('home')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Credential details do not exist')
            return redirect('signup')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
def admin(request):
    return redirect('admin')

# Create your views here.
