from django.urls import path, re_path
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView, GroupListView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    re_path(r'^tasks/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
    re_path(r'^tasks/(?P<pk>\d+)/update/$', TaskUpdateView.as_view(), name='task-update'),
    re_path(r'^tasks/(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='task-delete'),
    path('groups/', GroupListView.as_view(), name='group-list'),
]
