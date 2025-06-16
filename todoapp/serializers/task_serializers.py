from rest_framework import serializers
from ..models import todo

class Taskserializers(serializers.ModelSerializer):
    class Meta:
        model=todo.Todo
        fields="__all__"
        read_only_fields=('created','updated')