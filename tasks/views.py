from django.shortcuts import redirect, render, get_object_or_404

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
            title=title,
            description=description,
            priority=priority
        )

        return redirect("task_list")

    return render(request, "tasks/task_form.html")


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    context = {
        "task": task
    }

    return render(request, "tasks/task_detail.html", context)


def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.completed = request.POST.get("completed") == "on"

        task.save()

        return redirect("task_detail", task_id=task.id)

    context = {
        "task": task,
    }

    return render(request, "tasks/task_edit.html", context)


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()

        return redirect("task_list")

    context = {
        "task": task,
    }

    return render(
        request,
        "tasks/task_confirm_delete.html",
        context
    )