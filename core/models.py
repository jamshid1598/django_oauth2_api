from django.db import models

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='book-images/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url