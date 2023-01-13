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
from .serializers import UserSerializer
from apps.common.utils import validate_email
from apps.wallet.models import Wallet, DebitCard
from apps.common.id_generator import otp_generator
from apps.wallet.serializers import WalletSerializer, DebitCardSerializer


class HomeScreenViewSet(APIView):
    # serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Allows for a registered user to fetch his home screen data
        """
        try:
            wallet = Wallet.objects.filter(wallet_user=request.user.pkid).first()

            serializer = WalletSerializer(wallet)
            
            return Response(
                data={
                    "wallet": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"{e} :: an error occured")
            return Response(
                data={
                    "message": "An errror occured while fetch home screen data.",
                    "error": f"{e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


homescreen_viewset = HomeScreenViewSet.as_view()

class WalletScreenViewSet(APIView):
    # serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Allows for a registered user to fetch his wallet screen data
        """
        try:
            debitcards = DebitCard.objects.filter(card_user=request.user.pkid)

            serializer = DebitCardSerializer(debitcards, many=True)
            
            return Response(
                data={
                    "debitcards": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"{e} :: an error occured")
            return Response(
                data={
                    "message": "An errror occured while fetch wallet screen data.",
                    "error": f"{e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


walletscreen_viewset = WalletScreenViewSet.as_view()
