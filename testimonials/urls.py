from django.urls import path
from django.views.generic import RedirectView
from views import TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView

urlpatterns = [
    path('2023/02/32/', RedirectView.as_view(pattern_name='testimonials:index', permanent=True)),
    path('', TeacherListView.as_view(), name='teacher_list'),
    path('create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),
]
