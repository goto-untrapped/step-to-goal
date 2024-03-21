from django.db import models

class Goal(models.Model):
    name = models.TextField(max_length=100)
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.


#クラス名=テーブル名
#クラス変数=カラム名