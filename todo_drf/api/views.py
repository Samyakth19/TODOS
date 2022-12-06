from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls ={
        'Link':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
<<<<<<< Updated upstream
    return Response(api_urls)
=======
    return Response(api_urls)
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)

>>>>>>> Stashed changes
