from django.shortcuts import render

# Create your views here.

# users/views.py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class AdminLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        if not user.is_staff:
            token.delete()
            return Response({"error": "Admins only"}, status=403)
        return response
