from django.db import models
from django.utils import timezone

class Payment(models.Model):
    booking_reference = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')  # Pending, Completed, Failed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.booking_reference} - {self.status}"
