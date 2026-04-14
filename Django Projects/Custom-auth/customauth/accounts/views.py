from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from blog.models import Blog


def register_view(request):
    errors = []
    initial = {"full_name": "", "email": ""}

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        initial["full_name"] = full_name
        initial["email"] = email

        if not full_name or not email or not password1 or not password2:
            errors.append("All fields are required.")

        if password1 != password2:
            errors.append("Passwords do not match.")

        if email and CustomUser.objects.filter(email=email).exists():
            errors.append("Email already exists.")

        if not errors:
            user = CustomUser(full_name=full_name, email=email)
            user.set_password(password1)
            user.save()
            return redirect("login")

    return render(request, "register.html", {"errors": errors, "initial": initial})


def login_view(request):
    errors = []
    initial = {"email": ""}

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        initial["email"] = email

        if not email or not password:
            errors.append("Both email and password are required.")
        else:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                errors.append("Invalid email or password.")

    return render(request, "login.html", {"errors": errors, "initial": initial})


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    user_blogs = Blog.objects.filter(author=request.user)
    return render(
        request,
        'profile.html',
        {
            'user_obj': request.user,
            'blogs': user_blogs,
        },
    )

"""
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Login</h2>

{% if errors %}
    <ul style="color: red;">
        {% for error in errors %}
            <li>{{ error }}</li>
        {% endfor %}
    </ul>
{% endif %}

<form method="POST">
    {% csrf_token %}
    <p>
        <label for="id_email">Email:</label><br>
        <input type="email" id="id_email" name="email" value="{{ initial.email }}" required>
    </p>
    <p>
        <label for="id_password">Password:</label><br>
        <input type="password" id="id_password" name="password" required>
    </p>
    <button type="submit" style="width: 100%; height: 40px; border-radius: 5px; background-color: #2c3e50; color: white; border: none; cursor: pointer;">Login</button>
</form>

<p>Don't have an account?
    <a href="{% url 'register' %}">Register</a>
</p>
{% endblock %}

"""