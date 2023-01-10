from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from apps.common import validations
from apps.common.utils import validate_email
from apps.common.otp import send_verification_otp
from apps.common.id_generator import otp_generator
from .serializers import UserSerializer


class SignUpViewSet(APIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=[
                "first_name",
                "last_name",
                "email",
                "phone",
                "country",
                "password",
            ],
            properties={
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "phone": openapi.Schema(type=openapi.TYPE_STRING),
                "country": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            "201": openapi.Response(
                description="Success",
                examples={
                    "application/json": {
                        "id": "uuid",
                        "pkid": "number",
                        "first_name": "string",
                        "last_name": "string",
                        "email": "string",
                        "is_active": "boolean",
                        "account_activation_otp": "string",
                        "reset_password_otp": "string",
                    }
                },
            )
        },
    )
    def post(self, request):
        """
        Allows for a new user to create his/her account
        """
        if not validations.validate_signup(request.data):
            return Response(
                data={"message": validations.validator_message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if validate_email(request.data["email"]):
                data = {
                    "first_name": request.data["first_name"],
                    "last_name": request.data["last_name"],
                    "email": request.data["email"],
                    "phone": request.data["phone"],
                    "country": request.data["country"],
                    "password": request.data["password"],
                }

                serializer = self.serializer_class(data=data)

                if serializer.is_valid():
                    serializer.save()

                    token = otp_generator()

                    user = User.objects.get(email=serializer.data["email"])
                    user.account_activation_otp = token
                    user.save()

                    send_verification_otp(serializer.data["email"], token)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(
                data={"message": "Invalid email address."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(f"{e} :: an error occured")
            return Response(
                data={
                    "message": "An error occured while creating a new user",
                    "error": f"{e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


signup_viewset = SignUpViewSet.as_view()


class ActivateAccountViewSet(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=[
                "token",
            ],
            properties={"token": openapi.Schema(type=openapi.TYPE_STRING)},
        ),
    )
    def patch(self, request):
        """
        Allows for a new user to activate his/her account
        """
        if not validations.validate_activate_account(request.data):
            return Response(
                data={"message": validations.validator_message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            data = {
                "token": request.data["token"],
            }

            user = User.objects.get(account_activation_otp=data["token"])

            user.is_verified = True
            user.account_activation_otp = None
            user.save()

            return Response(
                data={"message": "Account verified successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"{e} :: an error occured")
            return Response(
                data={
                    "message": "An error occured while activating user",
                    "error": f"{e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


activate_viewset = ActivateAccountViewSet.as_view()


class SigninViewSet(APIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=[
                "email",
                "password",
            ],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            "200": openapi.Response(
                description="Success",
                examples={
                    "application/json": {
                        "user": {},
                        "access": "Bearer wiioo....",
                        "refresh": "uvdmiwi...",
                    }
                },
            )
        },
    )
    def post(self, request):
        """
        Allows for a registered user to signin
        """
        if not validations.validate_signin(request.data):
            return Response(
                data={"message": validations.validator_message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if validate_email(request.data["email"]):
                user = User.objects.filter(
                    Q(email=request.data["email"].strip())
                ).first()

                if user is None:
                    return Response(
                        data={"message": "Email is not registered!"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                if not user.check_password(request.data["password"]):
                    return Response(
                        data={"message": "Incorrect password"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                refresh__token = RefreshToken.for_user(user)
                access__token = "Bearer " + str(refresh__token.access_token)

                serializer = self.serializer_class(user)

                return Response(
                    data={
                        "user": serializer.data,
                        "access": access__token,
                        "refresh": str(refresh__token),
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"message": "Invalid email address."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(f"{e} :: an error occured")
            return Response(
                data={"message": "An errror occured during signin.", "error": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST,
            )


signin_viewset = SigninViewSet.as_view()
