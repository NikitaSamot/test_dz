from django.core import signing
from django.views import View
from django.shortcuts import render, redirect

from .forms import ItemForm, ContactForm, BBCodeForm, FileUploadForm
from .models import Item
from django.contrib import messages
from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile, Product, Subject, Student, Category
from django.contrib.auth.models import User
from django.utils.text import slugify
from reviews.models import Review


@login_required
def some_view(request):
    if request.user.is_authenticated:
        print(f"Пользователь: {request.user.username}")
        print(f"Авторизован: {request.user.is_authenticated}")
        print(f"Группы: {request.user.groups.all()}")
    else:
        print("Пользователь не авторизован")


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


def my_view(request):
    data = {
        'name': 'John',
        'age': 25,
        'items': ['Apple', 'Banana', 'Orange'],
    }
    return render(request, 'my_template.html', {'data': data})


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


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            return render(request, 'blog/success.html')
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})


def save_bbcode(request):
    data = {'key': 'value'}
    signed_data = signing.dumps(data)
    try:
        original_data = signing.loads(signed_data)
    except signing.BadSignature:
        original_data = None
    if request.method == 'POST':
        form = BBCodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Пример уведомления')
            return render(request, 'blog/success.html')
    else:
        form = BBCodeForm()
    return render(request, 'bbcode_form.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            FileUploadForm.objects.create(file=file)
            return redirect('upload_success')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(pre_save, sender=Product)
def update_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)


def subjects_students(request):
    subjects = Subject.objects.all()
    students = Student.objects.filter(subjects__isnull=False)
    context = {
        'subjects': subjects,
        'students': students
    }
    return render(request, 'subjects_student.html', context)


def index(request):
    categories = Category.objects.all()
    reviews = Review.objects.all()
    context = {
        'categories': categories,
        'reviews': reviews
    }
    return render(request, 'index.html', context)
