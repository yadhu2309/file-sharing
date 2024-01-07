from django.db import models
import uuid
from uuid import uuid4
import os
# Create your models here.

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now=True)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)


    
