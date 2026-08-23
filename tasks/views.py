from django.shortcuts import render
from .models import Task


def home(request):
    tasks = Task.objects.all()

    context = {
        "name": "Kaushal",
        "tasks": tasks,
    }

    return render(request, "tasks/home.html", context)