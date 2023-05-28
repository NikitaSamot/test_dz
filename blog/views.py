from django.views import View
from django.shortcuts import render, redirect
from .models import Item


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
        return render(request, 'create_item.html')

    def post(self, request):
        name = request.POST.get('name')
        return redirect('items')


class GroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'groups.html', {'groups': groups})


class CreateGroupView(View):
    def get(self, request):
        return render(request, 'create_group.html')

    def post(self, request):
        name = request.POST.get('name')
        return redirect('groups')
