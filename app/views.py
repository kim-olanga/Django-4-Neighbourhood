from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})