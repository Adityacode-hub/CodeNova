from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User=get_user_model()
def home(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,username=email,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            messages.error(request,"INVALID EMAIL OR PASSWORD")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dob = request.POST.get("date_of_birth")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1!=password2:
            messages.error(request,"password does not match")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,"email is already registered")
            return redirect('register')
        user=User.objects.create_user(email=email,phone=phone,date_of_birth=dob,password=password1)
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # URL name of your login page

    return render(request, "register.html")



User = get_user_model()

def password_change(request):
    if request.method == "POST":
        email = request.POST.get("email")
        old_password = request.POST.get("old_password")
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")

        try:
            user = User.objects.get(email=email)

            # Check old password
            if not user.check_password(old_password):
                messages.error(request, "Old password is incorrect.")
                return redirect("password_change")

            # Match new passwords
            if new_password1 != new_password2:
                messages.error(request, "New passwords do not match.")
                return redirect("password_change")

            # Set and save new password
            user.set_password(new_password1)
            user.save()
            messages.success(request, "Password changed successfully. Please login again.")
            return redirect("login")

        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return redirect("password_change")

    return render(request, "password_change.html")

@login_required
def profile(request):
    if request.method == 'POST' and request.FILES.get('image'):
        user = request.user
        user.image = request.FILES['image']
        user.save()
    return render(request, "users/profile.html", {"user": request.user})
