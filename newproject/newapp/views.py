from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# www.example.com/api/index

# @api_view(['GET'])
# def index(request):
#     people_detail = {
#         'name' : 'Praveen',
#         'age' : 32,
#         'job' : 'IT Fields'
#     }
#     return Response(people_detail)


# @api_view(['GET', 'POST', 'PUT'])
# def index(request):
#     if request.method == 'GET':
#         people_detail = {
#             'name' : 'Praveen',
#             'age' : 32,
#             'job' : 'IT Fields'
#         }
#         return Response(people_detail)
#     elif request.method == 'POST':
#         return Response("THIS IS A POST METHODS")
#     elif request.method == 'PUT':
#         return Response("THIS IS A PUT METHODS")
    


from .serializer import *
from .models import person

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def persons(request):
    if request.method == 'GET':
        objperson = person.objects.filter(team__isnull = False)
        # objperson = person.objects.all()
        serializer = PersonSerializer(objperson,  many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        obj = person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})



from rest_framework.views import APIView
# class ClassPerson(APIView):
#     def get(self,request):
#         return Response("This is a get method from APIView")
    

#     def post(self,request):
#         return Response("This is a post method from APIView")


class ClassPerson(APIView):

    def get(self,request):
        objperson = person.objects.all()
        serializer = PersonSerializer(objperson, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        data = request.data
        obj = person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
        data = request.data
        obj = person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


