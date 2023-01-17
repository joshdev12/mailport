from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from .form import IndexForm
from django.conf import settings

# Create your views here.

def index(request, *args, **kwargs):        

            
    form = IndexForm()
    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           
           html = render_to_string('html/form.html',{
               'name':name,
               'email':email,
               'subject':subject,
               'message':message
           })
           send_mail(
                'subject content',
                'message',
                'joshuaajayi@gmail.com',
                ['joshuaajayi012@gmail.com'],
                html_message=html
           )
            
        return redirect('index')
    else:
        
        form = IndexForm
        
    return render(request, "html/index.html", {'form':form})

def generic(request, *args, **kwargs):
    
    form = IndexForm()
    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           
           html = render_to_string('html/form.html',{
               'name':name,
               'email':email,
               'subject':subject,
               'message':message
           })
           send_mail(
                'subject content',
                'message',
                'joshuaajayi@gmail.com',
                ['joshuaajayi012@gmail.com'],
                html_message=html
           )
            
        return redirect('index')
    else:
        
        form = IndexForm
    
    return render(request, "html/generic.html",{"form":form})

def elements(request, *args, **kwargs):
    return render(request, "html/elements.html")