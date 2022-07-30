from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Snack(models.Model):
    name = models.CharField(max_length= 64, help_text="Snack Name", default="Snack")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='Description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])

