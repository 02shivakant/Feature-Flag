from  rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Organization , OrganizationMember
from .serializers import OrganizationSerializer

class OrganizationCreateView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        organization = serializer.save()

        OrganizationMember.objects.create(
            organization=organization,
            user=self.request.user,
            role='ADMIN'
        )