from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import task_serializers
from ..models import todo
from rest_framework.views import APIView



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
        serializer=task_serializers.Taskserializers(task)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer=task_serializers.Taskserializers(task,data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response({'message':"deleted"},status=status.HTTP_204_NO_CONTENT)
    
class MyModelApiView(APIView):
    def get_object(self, pk):
        try:
            return todo.Todo.objects.get(pk=pk)
        except todo.Todo.DoesNotExist:
            return None

    def get(self, request, pk=None):
        try:
            if pk:
                item = self.get_object(pk)
                if not item:
                    return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
                serializer = task_serializers.Taskserializers(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                tasks = todo.Todo.objects.all()
                if not tasks.exists():
                    return Response({"error": "No tasks found"}, status=status.HTTP_404_NOT_FOUND)
                serializer = task_serializers.Taskserializers(tasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = task_serializers.Taskserializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            task = self.get_object(pk)
            if not task:
                return Response({"error": "Item not found in DB"}, status=status.HTTP_404_NOT_FOUND)

            serializer = task_serializers.Taskserializers(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            item = self.get_object(pk)
            if not item:
                return Response({"error": "Item not found in DB"}, status=status.HTTP_404_NOT_FOUND)

            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

