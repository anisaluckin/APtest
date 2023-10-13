import re

from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from audienceplatformtest.models import User
from audienceplatformtest.serializers.registration import RegistrationSerializer


class Registration(GenericAPIView):
    """
    Register new user
    """

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if len(serializer.data['password']) < 6:
            return Response({"error": "Password must contain at least 6 characters"}, status=status.HTTP_400_BAD_REQUEST)
        elif not re.search('[a-zA-Z0-9]*', serializer.data['password'])\
                or not re.search('[a-zA-Z]', serializer.data['password']):
            return Response({"error": "Password must contain letters numbers"}, status=status.HTTP_400_BAD_REQUEST)
        user = User()
        user.set_password(serializer.data['password'])
        user.email = serializer.data['email'].lower()
        user.date_joined = timezone.now()
        user.is_active = True
        user.save()

        return Response({"success": "Registration successful"}, status=status.HTTP_201_CREATED)
