from  rest_framework import generics
from rest_framework.permissions import AllowAny


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import RegisterSerializers

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_class = [AllowAny]

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email
        }

        )