from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignupForm, LoginForm,EditProfileForm
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
    return render(request, 'index.html')

def signup(request):
    # your signup logic here
    return render(request, 'signup.html')



def doctor_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_type = 'doctor'  # 🔁 force doctor
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def patient_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_type = 'patient'  # 🔁 force patient
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    context = {
        'user': request.user,
        'year': datetime.datetime.now().year,
    }
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # or wherever you want after saving
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})