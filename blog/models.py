from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


group = Group.objects.get(name='Пользователи с доступом ко всему функционалу')
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    group.user_set.add(user)


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
