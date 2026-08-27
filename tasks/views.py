from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    status = request.GET.get("status")
    priority = request.GET.get("priority")
    sort = request.GET.get("sort")

    tasks = Task.objects.all()

    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    if sort == "oldest":
        tasks = tasks.order_by("created_at")
    elif sort == "due_date":
        tasks = tasks.order_by("due_date")
    else:
        tasks = tasks.order_by("-created_at")

    context = {
        "name": "Kaushal",
        "tasks": tasks,
    }

    return render(request, "tasks/home.html", context)


def task_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("task_list")

    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_form.html", context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    context = {
        "task": task
    }

    return render(request, "tasks/task_detail.html", context)


def task_edit(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect("task_detail", task_id=task.id)

    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
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