from rest_framework import serializers
from .models import Goal, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'content', 'todos']  # モデルのフィールドを指定します



class GoalSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)  # ネストされたシリアライザーを使用します
    name = serializers.TextField(max_length=100)
    content = serializers.TextField(max_length=100)
    class Meta:
        model = Goal
        fields = ['id', 'name', 'content', 'todos']  # モデルのフィールドを指定します
    def create(self, validated_data):
        
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        return instance