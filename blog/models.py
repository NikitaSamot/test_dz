from django.db import models
from django.apps import AppConfig
from django.db.models.signals import post_migrate
# Create your models here.


def add_superuser_to_group(sender, **kwargs):
    Group = sender.get_model('auth', 'Group')
    User = sender.get_model('auth', 'User')

    group = Group.objects.get(name='Пользователи с доступом ко всему функционалу')
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        group.user_set.add(user)


class CustomersConfig(AppConfig):
    name = 'customers'

    def ready(self):
        post_migrate.connect(add_superuser_to_group, sender=self)


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


products = Product.objects.prefetch_related('category')
# В результате использования метода prefetch_related() с указанием правильного имени поля можно
# значительно повысить производительность и сократить количество запросов к базе данных при работе
# с моделью, описывающей товар, и её связанными объектами или данными.


class BBCode(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')