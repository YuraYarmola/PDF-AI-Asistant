from django.db import models

from users.models import Profile


class UploadedFile(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
