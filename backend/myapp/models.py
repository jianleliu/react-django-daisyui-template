from django.db import models

# Create your models here.
# myapp/models.py


class MyApp(models.Model):
    # Define fields here
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
