from django.db import models


# Create your models here.

class UserTable(models.Model):
    name = models.CharField(max_length=256, null=True)
    gender = models.CharField(max_length=256, choices=[("m", '男性'), ('f', '女性')], default='m')
    comment = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    age = models.PositiveIntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True)

    class Meta:
        db_table = 'test_user'
