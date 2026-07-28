import requests
from django.shortcuts import render 


def all_users(request):

    response = requests.get("https://backend-9iqu.vercel.app/users")

    data = response.json()

    context = {
        "users": data["users"]
    }

    return render(request, "home.html", context)


def user_detail(request, user_id):

    response = requests.get(
    f"https://backend-9iqu.vercel.app/users/{user_id}"
)
    data = response.json()

    context = {
        "user": data
    }

    return render(request, "user_detail.html", context)