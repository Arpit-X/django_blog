from django.shortcuts import render,redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articlesList(request):
    articles=Articles.objects.all().order_by("date")
    return render(request,'articles/articlesList.html',{"articles":articles})

def articleDetails(request,slug):
    article=Articles.objects.get(slug=slug)
    return render(request,'articles/articleDetail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def articleCreate(request):
    if request.method=='POST':
        form=forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticles()
    return render(request,'articles/articleCreate.html',{'form':form})
