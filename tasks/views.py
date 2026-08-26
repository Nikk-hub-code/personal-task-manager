from django.shortcuts import redirect, render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    context = {
        "name": "Kaushal",
        "tasks": tasks,
    }

    return render(request, "tasks/home.html", context)

def task_create(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")

        Task.objects.create(
            title = title,
            description = description,
            priority = priority
        )

        return redirect("task_list")

    return render(request, "tasks/task_form.html")