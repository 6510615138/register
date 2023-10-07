from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignInViaUsernameForm


def getUsername(request):
    if request.method == 'POST':
        form = SignInViaUsernameForm(request.POST)
        if form.is_valid():
            form.login(request,)
            return HttpResponseRedirect("subject/")
    else:
        
        form = SignInViaUsernameForm()

    return render(request,'login.html',{"form":form})
