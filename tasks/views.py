from django.shortcuts import redirect, render
from .models import Task


def home(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")

        Task.objects.create(
            title=title,
            description=description,
            priority = priority
        )

        return redirect("home")

    tasks = Task.objects.all()

    context = {
        "name": "Kaushal",
        "tasks": tasks,
    }

    return render(request, "tasks/home.html", context)