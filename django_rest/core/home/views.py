from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *



@api_view(['GET'])
def home(request):
    student_data = Student.objects.all()
    #serializing data to avoid errors

    serializers = StudentSerializer(student_data, many = True)
    return Response(
        {
            'status' : 200,
            'message' : 'Hello From Yugam',
            'data' : serializers.data
        }
    )

@api_view(['POST'])
def post_student(request):
    data = request.data
    
    serializer = StudentSerializer(
        data = request.data
    )

    if not serializer.is_valid():
        return Response({
            'status' : 403,
            'message' :'Something went wrong',
            'success' : False,
            'error' : serializer.errors
        })
    
    serializer.save()

    return Response({
        'status' : 200,
        'data' : serializer.data,
        'message' : 'Student added successfully',
        'success' : True
    })

@api_view(['PUT', 'PATCH'])
def update_student(request, id):
    try:
        student_data = Student.objects.get(id = id)
        serializers = StudentSerializer(student_data, data = request.data, partial = True)
        
        if not serializers.is_valid():
            return Response({
                'status' : 403,
                'message' : 'Something went wrong',
                'errors' : serializers.errors,
                'success' : False
            })
        
        serializers.save()
        return Response({
            'status' : 200,
            'data' : serializers.data,
            'message' : 'Student updated successfully',
            'success' : True
        })
    except Exception as e:
        return Response({
            'status' : 403,
            'message' : 'invallid id',
            'success' : False,
            'error' : e
        })
    

@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_data = Student.objects.get(id = id)
        student_data.delete()

        return Response({
            'status' : 200,
            'message' : 'User deleted successfully',
            'success' : True
        })
    except Exception as e :
        return Response({
            'status' : 403,
            'message' : 'invallid id',
            'success' : False,
            'error' : e
        })