from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.base import View

from django.contrib import messages
from login.forms import UserRegistrationForm


# class Register(CreateView):
#     form_class = UserCreationForm
#     success_url = 'login'
#     template_name = 'register.html'

def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            print('is valid')
            return redirect('/login')
    else:
        form = UserRegistrationForm()
        print('is not valid')
    return render(request, 'register.html', {'form': form})


class Logout(View):
    def qet(self, request):
        return render(request, '')


