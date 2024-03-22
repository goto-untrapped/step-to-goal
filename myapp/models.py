from django.db import models

class Goal(models.Model):
    name = models.TextField(max_length=100)
    content = models.TextField(max_length=100)
    """ def __str__(self):
        return self.name """
    
class Todo(models.Model):
    goal = models.ForeignKey(Goal, related_name='todos', on_delete=models.CASCADE)
    #Todoインスタンスが特定のGoalインスタンスに関連付けられることを可能にする
    content = models.CharField(max_length=100)
# Create your models here.


#クラス名=テーブル名
#クラス変数=カラム名