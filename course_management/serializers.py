from rest_framework import serializers

from course_management.models import Course

from module_management.models import Module

class CourseSerializer(serializers.ModelSerializer):

    module_count= serializers.SerializerMethodField(read_only=True) # this is not present in course model,
                                                                    # but we need to display when courses is listed
                                                                    # defined in   get_module_count

    class Meta:
         model=Course
         fields='__all__'
         read_only_fields=["id","trainer","slug","created_at","updated_at"]

    def get_module_count(self,obj):

         return Module.objects.filter(course=obj).count()

         