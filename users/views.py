from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'registration/signup.html', {'form': form})
