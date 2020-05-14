# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import forms

# Create your views here.
def signup_view(request):
    if (request.method =='POST'):
        form=forms.UserCreationForm(request.POST) #isse jo dataa aaya post request k saath usse form bnega and saved in form
        if (form.is_valid()):
            form.save()
            return redirect('articles:list')
        
    else:  # request is get.. so what u do is .. take the required form and send it in the template 
        form=forms.UserCreationForm()
    return render(request,'signup_page.html',{'form_info':form})  # by default request is get.. 