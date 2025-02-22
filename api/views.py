from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CourseDetail, CustomToken, UserDailyActivity
from .serializers import CourseDetailSerializer, CouponDetailPagination

class CourseDetailListAPIView(generics.ListAPIView):
    queryset = CourseDetail.objects.select_related("coupon").all()
    serializer_class = CourseDetailSerializer
    pagination_class = CouponDetailPagination

    def get(self, request, *args, **kwargs):
        today = now().date()
        user = request.user
        activity, _ = UserDailyActivity.objects.get_or_create(user=user, date=today)
        activity.request_count+=1
        activity.save()

        return super().get(request, *args, **kwargs)

    
def home(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        token, _ = CustomToken.objects.get_or_create(user=user)
        context = {"token": token.key}
    return render(request, "home.html", context=context)