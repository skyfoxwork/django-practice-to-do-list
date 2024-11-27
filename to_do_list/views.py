from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_list.models import Task, Tag


def index(request):
    task_list = Task.objects.all()
    context = {
        "task_list": task_list
    }
    return render(request, "to_do_list/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("tags")


class AddTaskView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "tags", "done")
    success_url = reverse_lazy("to_do_list:index")


class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags", "done")
    success_url = reverse_lazy("to_do_list:index")


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:index")


def complete_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        print(task.content)
        print(task.done)
        task.done = False
        task.save()

    return redirect("to_do_list:index")


def undo_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.done = True
        task.save()

    return redirect("to_do_list:index")


class TegListView(generic.ListView):
    model = Tag


class AddTagView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("to_do_list:tag-list")


class UpdateTagView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("to_do_list:tag-list")


class DeleteTadView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tag-list")
