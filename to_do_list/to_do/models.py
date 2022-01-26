from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    """
    Class-based Model for the activty
    Fields:
        1. Title
        2. Descriptioon
    """

    title = models.CharField(max_length=100)
    description = models.TextField()

    due_date = models.DateTimeField(verbose_name="Date Due",default=timezone.now)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass
        #unique_together=((title,due_date))

    def __str__(self):
        """
        String represnetation of instance with more context

        Check the date to determine if the task has passed or is upcoming
        """

        if self.due_date < timezone.now():
            state = "(Past)"
        elif timezone.now() - self.due_date < timedelta(days=7):
            state = "(Upcoming)"
        return f"{self.title} -{self.due_date} {state}"

    
    def get_absolute_url(self):
        return reverse("to_do:detail_view",args=[self.pk])