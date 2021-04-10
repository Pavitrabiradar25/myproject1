from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm
from django.views import View
from .models import *



def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})

def ajax_posting(request):
    if request.is_ajax():
        email = request.POST.get('email', None) 
        password = request.POST.get('password', None) 
        if email and password: 
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON
