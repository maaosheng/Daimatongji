from django.db import models

# Create your models here.
class  Userinfo(models.Model):
    name = models.CharField(max_length=36)
    date = models.CharField(max_length=36)
    num = models.CharField(max_length=128,null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together=(
            ('name','date')
        )