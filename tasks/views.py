from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    status = request.GET.get("status")
    priority = request.GET.get("priority")
    sort = request.GET.get("sort")

    tasks = Task.objects.filter(user=request.user)

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

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    pending_tasks = tasks.filter(status="pending").count()
    in_progress_tasks = tasks.filter(status="in_progress").count()
    completed_tasks = tasks.filter(status="completed").count()
    high_priority_tasks = tasks.filter(priority="high").count()

    active_tasks = tasks.exclude(status="completed").order_by("due_date")
    completed_task_list = tasks.filter(status="completed").order_by("-updated_at")

    today = timezone.localdate()

    today_tasks = tasks.filter(due_date=today).exclude(status="completed")

    overdue_tasks = tasks.filter(
        due_date__lt=today
    ).exclude(
        status="completed"
    )

    context = {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
        "completed_tasks": completed_tasks,
        "high_priority_tasks": high_priority_tasks,
        "active_tasks": active_tasks,
        "completed_task_list": completed_task_list,
        "today_tasks": today_tasks,
        "overdue_tasks": overdue_tasks,
    }

    return render(request, "tasks/dashboard.html", context)

@login_required
def task_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")

    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_form.html", context)


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    context = {
        "task": task
    }

    return render(request, "tasks/task_detail.html", context)

@login_required
def task_edit(request, task_id):

    task = get_object_or_404(Task, id=task_id, user=request.user)

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

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

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