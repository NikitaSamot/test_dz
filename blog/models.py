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
