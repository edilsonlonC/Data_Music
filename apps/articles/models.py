from django.db import models
from apps.instruments.models import Material
from apps.mark.models import Mark

# Create your models here.

class Article (models.Model):
    Description=models.CharField(max_length=25)
    precio=models.FloatField()
    id_mark=models.ForeignKey(Mark,on_delete=models.CASCADE,null=True)
    Id_Material=models.ForeignKey(Material,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Description
