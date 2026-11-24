from django.shortcuts import render,get_object_or_404

from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from course_management.serializers import CourseSerializer
from course_management.models import Course
from course_management.permissions import IsOwner
# Create your views here.

class CourseCreateListView(APIView) :
    ##ListAPIView can be used instead of ApiView in the above inheritence

    #serializer_class=CourseSerializer

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    # overriding get_queryset method to list authorized user courses only
    # def get_queryset(self):
    #     return Course.objects.filter(trainer=self.request.user)
    
    def get(self,request):

        qs= Course.objects.filter(trainer=request.user)
        serializer_instance=CourseSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):

        form_data= request.data
        serializer_instance= CourseSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(trainer=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class CourseRetreiveUpdateDeleteView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk=None):
         qs= get_object_or_404(Course,id=pk)
         serializer_instance=CourseSerializer(qs)
         return Response(serializer_instance.data)  

    def patch(self,request,pk=None):  # using patch 

        form_data=request.data
        instance= get_object_or_404(Course,id=pk)
        serialzer_instance=CourseSerializer(data=form_data,instance=instance,partial=True)
        if serialzer_instance.is_valid():
            serialzer_instance.save()
            return Response(serialzer_instance.data)
        else:
            return Response(serialzer_instance.errors)

    def delete(self,request,pk=None):
        instance=get_object_or_404(Course,id=pk)
        instance.delete()
        return Response({"message":"deleted"})