from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(username=data['user_name'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'], password=data['password_1'])
            return redirect('home:home')
    else:
        form = UserRegisterForm() 
    contxt = {'form':form}
    return render(request, 'Accounts/register.html', contxt)

