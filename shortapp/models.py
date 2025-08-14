from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import string, random

class Link(models.Model):
    code = models.CharField(max_length=16, unique=True, db_index=True)
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    custom = models.BooleanField(default=False)

    def is_expired(self):
        return self.expires_at and timezone.now() > self.expires_at

    @staticmethod
    def generate_code(length=7):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def __str__(self):
        return f"{self.code} → {self.long_url}"
