from django.db import models

# Create your models here.
class thread(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    timestap=models.DateTimeField(auto_now=False,auto_now_add=True)
def __str__(self):
    return self.title()
