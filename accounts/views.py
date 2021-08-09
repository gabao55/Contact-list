from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Invalid username and/or password.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login successful.')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeatpassword = request.POST.get('repeatpassword')

    if not email or not username or not password or not repeatpassword:
        messages.error(request, 'Please fill all the fields.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email.')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Password too short (at least 6 characters).')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Username too short (at least 6 characters).')
        return render(request, 'accounts/register.html')

    if password != repeatpassword:
        messages.error(request, 'The fields password and repeat password must be the same.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already registered.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email already registered.')
        return render(request, 'accounts/register.html')

    messages.success(request, "Registration successful.")

    user = User.objects.create_user(username=username, email=email,
                                    password=password, first_name=name, last_name=surname)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContact(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'An error has occurred on sending the form.')
        form = FormContact(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contact {request.POST.get("name")} saved successfully.')
    return redirect('dashboard')