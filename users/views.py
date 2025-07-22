from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Datos incompletos'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Usuario ya existe'}, status=400)

        User.objects.create_user(username=username, password=password)
        return Response({'message': 'Registro exitoso'}, status=201)
