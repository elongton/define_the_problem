from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver

class Feedback(models.Model):
    author = models.ForeignKey(User)
    anonymous_author = models.BooleanField(default=False)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('feedback:feedback_thanks')

    def __str__(self):
        return str(self.text) + '-' + str(self.author)
