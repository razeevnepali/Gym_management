from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image

# Create your models here.
class CustomUsers(AbstractUser):
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    PACKAGE = (
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    )
    package = models.CharField(max_length=20,choices=PACKAGE, default=1)
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width >300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path) 

class Profile(models.Model):

    user = models.OneToOneField(CustomUsers, on_delete=models.CASCADE, related_name='Profile')
    image = models.ImageField(default='media\default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'    


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) 

# class Registration(models.Model):
#     user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
#     PACKAGE_CHOICES = (
#         ('1', '1 Month'),
#         ('3', '3 Months'),
#         ('6', '6 Months'),
#         ('12', '12 Months'),
#     )
#     package = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
#     started_date = models.DateTimeField()







       