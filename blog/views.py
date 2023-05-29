from django.views import View
from django.shortcuts import render, redirect

from .forms import ItemForm, ContactForm
from .models import Item
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Делайте что-то с валидными данными формы
            return redirect('contact_success')
        else:
            # Вывод сообщения об ошибке
            messages.error(request, 'Ошибка ввода данных.')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})


def admin_contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Делайте что-то с валидными данными формы
            return redirect('admin_contact_success')
        else:
            # Вывод сообщения об ошибке
            messages.error(request, 'Ошибка ввода данных.')
    else:
        form = ContactForm()
    return render(request, 'admin_contacts.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class ItemView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'items.html', {'items': items})


class CreateItemView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'create_item.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
        return render(request, 'create_item.html', {'form': form})


class EditItemView(View):
    def get(self, request, item_id):
        item = Item.objects.get(id=item_id)
        form = ItemForm(instance=item)
        return render(request, 'edit_item.html', {'form': form, 'item': item})

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
        return render(request, 'edit_item.html', {'form': form, 'item': item})


class DeleteItemView(View):
    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        item.delete()
        return redirect('items')


class GroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'groups.html', {'groups': groups})


class CreateGroupView(View):
    def get(self, request):
        form = GroupForm()
        return render(request, 'create_group.html', {'form': form})

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        return render(request, 'create_group.html', {'form': form})


class EditGroupView(View):
    def get(self, request, group_id):
        group = Group.objects.get(id=group_id)
        form = GroupForm(instance=group)
        return render(request, 'edit_group.html', {'form': form, 'group': group})

    def post(self, request, group_id):
        group = Group.objects.get(id=group_id)
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
        return render(request, 'edit_group.html', {'form': form, 'group': group})


class DeleteGroupView(View):
    def post(self, request, group_id):
        group = Group.objects.get(id=group_id)
        group.delete()
        return redirect('groups')






