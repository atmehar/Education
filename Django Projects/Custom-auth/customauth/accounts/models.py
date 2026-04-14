from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            full_name=full_name,
        )

        user.set_password(password)  # ye password ko hash me convert kry ga
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Custom Auth{% endblock %}</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #2c3e50;
            padding: 15px 20px;
            color: white;
        }

        .navbar h2 {
            margin: 0;
        }

        .navbar-links {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 8px 12px;
            background-color: #e74c3c;
            border-radius: 5px;
        }

        .navbar a:hover {
            background-color: #c0392b;
        }

        .container {
            justify-content: center;
            align-items: center;
            display: flex;
            flex-direction: column;
            padding: 40px;
            margin: 40px auto;
            border: 1px solid black;
            border-radius: 10px;
            box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
            width: 50%;
            height: 50%;
        }

        button {
            padding: 8px 12px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <!-- Navbar -->
    <div class="navbar">
        <h2>Custom Auth Project</h2>

        <div class="navbar-links">
            {% if request.user.is_authenticated %}
                <a href="{% url 'blog_list' %}">Blogs</a>
                <a href="{% url 'my_blogs' %}">My Blogs</a>
                <a href="{% url 'blog_create' %}">New Blog</a>
                <a href="{% url 'profile' %}">Profile</a>
                <a href="{% url 'logout' %}">Logout</a>
            {% else %}
                <a href="{% url 'blog_list' %}">Blogs</a>
                <a href="{% url 'login' %}">Login</a>
                <a href="{% url 'register' %}">Register</a>
            {% endif %}
        </div>
    </div>

    <!-- Page Content -->
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>

</body>
</html>
"""