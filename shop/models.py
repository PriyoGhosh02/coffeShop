
# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Assuming users are registered and logged in

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking to user model (if you want user-based cart)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.name}"
    
    def save(self, *args, **kwargs):
        # Calculate total price for each item (price * quantity)
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
