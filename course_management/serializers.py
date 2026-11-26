from rest_framework import serializers

from course_management.models import Course

from module_management.models import Module
from module_management.serializers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    module_count= serializers.SerializerMethodField(read_only=True) # this is not present in course model,
                                                                    # but we need to display when courses is listed
                                                                    # defined in   get_module_count

    module= serializers.SerializerMethodField(read_only=True) # to add a field which is not present in course model


    class Meta:
         model=Course
         fields='__all__'
         read_only_fields=["id","trainer","slug","created_at","updated_at"]

    def get_module_count(self,obj):

         return Module.objects.filter(course=obj).count()

    def get_module(self,obj):  # This fn returns only PYNT

         qs= Module.objects.filter(course=obj) # obj refers to Course Model

         serializer_instance=ModuleSerializer(qs,many=True)

         return serializer_instance.data

         