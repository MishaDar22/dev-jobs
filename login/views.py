from django.shortcuts import render, redirect
from django.views.generic.base import View

from login.forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
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
