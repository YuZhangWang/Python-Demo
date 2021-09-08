from django.shortcuts import render, redirect
from . import models


def register(request):
    if request.method == 'POST':
        data = models.userdata()
        data.email = request.POST['email']
        data.password = request.POST['password']
        data.username = request.POST['username']
        try:
            data.save()
        except Exception:
            return render(request, 'error.html')
        return render(request, 'success.html')
    elif request.method == 'GET':
        return render(request, 'register.html')
