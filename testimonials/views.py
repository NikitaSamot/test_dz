from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView


# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'subject']


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'subject']


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse('teachers:teacher_list')
