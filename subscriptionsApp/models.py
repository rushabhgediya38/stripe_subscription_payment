from django.db import models
from django.contrib.auth.models import User


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255, blank=True, null=True)
    stripeSubscriptionId = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
