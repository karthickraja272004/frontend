import requests
from django.shortcuts import render 


def all_users(request):

    response = requests.get("http://flask-docker:8080/users")

    data = response.json()

    context = {
        "users": data["users"]
    }

    return render(request, "home.html", context)


def user_detail(request, id):

    response = requests.get(f"http://flask-docker:8080/users/{id}")
    data = response.json()

    context = {
        "user": data
    }

    return render(request, "user_detail.html", context)