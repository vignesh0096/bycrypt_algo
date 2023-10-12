from django.shortcuts import render
import bcrypt
from rest_framework.generics import CreateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status


class UserRegistration(CreateAPIView):
    serializer_class = UserCustomSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(email=request.data['email'])
            serializer = UserSerializer(data=request.data)
            if user:
                return Response('You are already registered')
            else:
                password = request.data['password']
                # salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                if serializer.is_valid():
                    User.objects.create(name=serializer.data['name'], email=serializer.data['email'],
                                        password=hashed)

                    return Response({'response_code': status.HTTP_200_OK,
                                     'message': "Registered successfully",
                                     'status_flag': True,
                                     'status': "success",
                                     'error_details': None,
                                     'data': []})
                else:
                    return Response({'response_code': status.HTTP_400_BAD_REQUEST,
                                     'message': 'Enter valid details',
                                     'status_flag': False,
                                     'status': 'Failed',
                                     })

        except Exception as e:
            return Response({'response_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': "cant register",
                             'status_flag': False,
                             'status': "Failed",
                             'error_details': str(e),
                             'data': []})


class Login(CreateAPIView):
    serializer_class = LoginCustomSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.data['email'])
            hashed_password = user.password
            password = request.data['password'].encode('utf-8')
            if bcrypt.hashpw(password, bcrypt.gensalt()) == hashed_password:
                serializer = LoginSerializer(instance=user)
                return Response(serializer.data)
            # if serializer.is_valid():
            #     mail = User.objects.get(email=request.data['email'])
            #     password = serializer.validated_data['password']
            #     hashed_password = mail.password
            #     check_password = bcrypt.checkpw(b"password", hashed_password)
            #     if check_password:
            return Response({
                            'response_code': status.HTTP_200_OK,
                            'message': "logged in succesfully",
                            'status_flag':True,
                            'status': "success",
                            'error_details': None,
                            })
            #
            # return Response({
            #                 'response_code': status.HTTP_400_BAD_REQUEST,
            #                 'message': "Enter valid details",
            #                 'status_flag':True,
            #                 'status': "Failed",
            #                 'data' : serializer.data,
            #                 'error_details': None,
            #                 })
        except Exception as e:
            return Response({'response_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': "something went wrong",
                             'status_flag': False,
                             'status': "Failed",
                             'error_details': str(e),
                             })
