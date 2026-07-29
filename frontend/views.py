import requests
from django.conf import settings
from django.shortcuts import render


def all_users(request):
    response = requests.get(settings.BACKEND_URL + "/users")

    data = response.json()

    context = {
        "users": data["users"]
    }

    return render(request, "home.html", context)


def user_detail(request, user_id):
    response = requests.get(f"{settings.BACKEND_URL}/users/{user_id}")

    data = response.json()

    context = {
        "user": data
    }

    return render(request, "user_detail.html", context)