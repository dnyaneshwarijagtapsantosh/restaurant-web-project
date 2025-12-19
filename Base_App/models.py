from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name


class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField()
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name


class AboutUs(models.Model):
    Description = models.TextField()


class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField()
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True)

    def __str__(self):
        return self.User_name


from django.db import models

class BookTable(models.Model):
    Name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=15)
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Items, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.item.Item_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    delivery_address = models.TextField()
    payment_method = models.CharField(max_length=20)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
