from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import task_serializers
from ..models import todo



@api_view(['GET','POST'])
def todo_manager(request):
    if request.method == 'POST':
        print("coming here")
        serializer=task_serializers.Taskserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer=task_serializers.Taskserializers(todo.Todo.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def todo_manager_crud(request,pk):
    try:
        task=todo.Todo.objects.get(pk=pk)
    except todo.Todo.DoesNotExist:
        return Response({'error':"Task Not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=task_serializers.Taskserializers()