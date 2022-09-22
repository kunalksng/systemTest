from django.db import models

# Create your models here.
class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    email = models.TextField()

    def __str__(self):
        return str(self.id)


