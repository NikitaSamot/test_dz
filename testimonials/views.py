from msilib.schema import ListView

from Tools.scripts.make_ctype import method
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import Genre
from .serializers import GenreSerializer

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


class CustomMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

    def some_method(self):
        pass


class CustomMixin2(LoginRequiredMixin, TemplateView):
    template_name = 'custom_template.html'

    def some_method(self):
        pass


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreViewSetTwo(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    @action(detail=True, method=['get'])
    def custom_action(self, request, pk=None):
        genre = self.get_object()
        return Response({'message': 'Custom Genre executed successfully'})


@transaction.atomic
def create_order(user, items):
    try:
        with transaction.atomic():
            order = Order(user=user)
            order.save()

            for item_data in items:
                product = Product.objects.get(id=item_data['product_id'])
                quantity = item_data['quantity']
                order_item = OrderItem(order=order, product=product, quantity=quantity)
                order_item.save()

            payment_successful = process_payment(order)

            if not payment_successful:
                raise Exception('Payment failed')

            send_order_confirmation(order)

        return order
    except Exception as e:
        transaction.set_rollback(True)
        raise e
