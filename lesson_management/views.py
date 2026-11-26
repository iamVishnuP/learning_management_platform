from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions

from module_management.models import Module

from lesson_management.serializiers import LessonSerializer
from lesson_management.models import Lesson

# Create your views here.

class LessonCreateView(CreateAPIView):
    serializer_class=LessonSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        module_id= self.kwargs.get("pk")
        module_object=get_object_or_404(Module,id=module_id)


        serializer.save(module=module_object,created_by=self.request.user)


class LessonRetreiveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=LessonSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Lesson.objects.all()
    
    