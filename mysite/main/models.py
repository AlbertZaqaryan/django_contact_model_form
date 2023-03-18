from django.db import models

# Create your models here.


class Phone(models.Model):

    model = models.CharField('Phone model', max_length=30)
    img = models.ImageField('Phone image', upload_to='images')
    price = models.PositiveBigIntegerField('Phone price')

    def __str__(self):
        return self.model
    

class About(models.Model):

    about = models.TextField('About us')



class Contact(models.Model):

    user_name = models.CharField('User name',  max_length=60)
    user_email = models.EmailField('User email', unique=True)
    user_phone = models.CharField('User phone',  max_length=60)
    user_reviw = models.TextField('USer review')

    def __str__(self):
        return self.user_name