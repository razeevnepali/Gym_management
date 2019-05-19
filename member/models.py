from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import CustomUsers


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    #For semantic analysis
    pos = models.DecimalField(decimal_places = 3, max_digits = 10, null = True, blank= True)
    neg = models.DecimalField(decimal_places = 3, max_digits = 10, null = True, blank = True )
    neutral = models.DecimalField(decimal_places = 3, max_digits = 10, null= True, blank = True)
    compound = models.DecimalField(decimal_places = 3,max_digits = 10, null = True, blank = True)
    
    #For recommendation
    cardio = models.BooleanField(default=False)
    strength = models.BooleanField(default=False)
    weight_loss = models.BooleanField(default=False)
    nutrition = models.BooleanField(default=False)
    mental_health = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





