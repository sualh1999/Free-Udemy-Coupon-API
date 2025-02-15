from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CourseDetail, CustomToken
from .serializers import CourseDetailSerializer, CouponDetailPagination

class CourseDetailListAPIView(generics.ListAPIView):
    queryset = CourseDetail.objects.select_related("coupon").all()
    serializer_class = CourseDetailSerializer
    pagination_class = CouponDetailPagination

class GenerateTokenAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        token, created = CustomToken.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)