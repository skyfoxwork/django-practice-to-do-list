from django.urls import path

from to_do_list.views import (
    index,
    TaskListView,
    AddTaskView,
    UpdateTaskView,
    DeleteTaskView,
    complete_task,
    undo_task,
    TegListView,
    AddTagView,
    UpdateTagView,
    DeleteTadView,
)

urlpatterns = [
    path("", index, name="index"),
    path("task-list/", TaskListView.as_view(), name="task-list"),
    path("create/", AddTaskView.as_view(), name="add-task"),
    path("update/<int:pk>/", UpdateTaskView.as_view(), name="update-task"),
    path("delete/<int:pk>/", DeleteTaskView.as_view(), name="delete-task"),
    path("complete/<int:pk>/", complete_task, name="complete-task"),
    path("undo/<int:pk>/", undo_task, name="undo-task"),
    path("tag-list/", TegListView.as_view(), name="tag-list"),
    path("create-tag/", AddTagView.as_view(), name="add-tag"),
    path("update-tag/<int:pk>/", UpdateTagView.as_view(), name="update-tag"),
    path("delete-tag/<int:pk>/", DeleteTadView.as_view(), name="delete-tag"),
]

app_name = "to_do_list"
