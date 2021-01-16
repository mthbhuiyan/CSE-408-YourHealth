from django.db import models
from accounts.models import User
from shop.models import Product


class Order(models.Model):
    ORDER_STATUS = (
        ('PND', 'Pending'),
        ('OTW', 'OnTheWay'),
        ('DLV', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    latitude = models.FloatField(default=23.7)
    longitude = models.FloatField(default=90.4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default='PND')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
