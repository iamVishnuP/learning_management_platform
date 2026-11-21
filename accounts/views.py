from django.shortcuts import render

from accounts.serializers import TrainerSerializer,TrainerProfileSerializer
from accounts.models import TrainerProfile

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
# Create your views here.
class TrainerSignUpView(CreateAPIView):
    serializer_class=TrainerSerializer
    

class TrainerRetreiveUpdateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        auth_user=request.user
        qs= TrainerProfile.objects.get(user=auth_user)
        serializer_instance=TrainerProfileSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request):
        instance=TrainerProfile.objects.get(user=request.user)
        form_data=request.data
        serializer_insatnce=TrainerProfileSerializer(data=form_data,instance=instance)
        if serializer_insatnce.is_valid():
            serializer_insatnce.save()
            return Response(serializer_insatnce.data)
        else:
            return Response(serializer_insatnce.errors)

    