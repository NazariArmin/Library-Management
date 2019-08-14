from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    published_date = models.DateField()
    count = models.IntegerField(default=1)
    category_name = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.book_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    birthday_date = models.DateField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    book = models.ForeignKey(Book, default=0, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    profile = models.OneToOneField(Profile, default=0, null=True, on_delete=models.SET_NULL)


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
