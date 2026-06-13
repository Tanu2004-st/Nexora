from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 100)
    description = models.TextField()
    author = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to = 'notes/', blank=True, null=True)

    def __str__(self):
        return self.title