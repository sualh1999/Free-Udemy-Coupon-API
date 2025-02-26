import json
import math
from django.shortcuts import render
from django.utils.timezone import now
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import Throttled

from .models import CourseDetail, Coupon, CustomToken, UserDailyActivity
from .serializers import CourseDetailSerializer, CouponDetailPagination

def update_user_activity(user):
    today = now().date()
    activity, _ = UserDailyActivity.objects.get_or_create(user=user, date=today)
    activity.request_count+=1
    activity.save()

class CourseDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CourseDetail.objects.select_related("coupon").all()
    serializer_class = CourseDetailSerializer

    def get(self, request, *args, **kwargs):
        update_user_activity(request.user)
        return super().get(request, *args, **kwargs)

class CourseDetailListAPIView(generics.ListAPIView):
    queryset = CourseDetail.objects.select_related("coupon").all().order_by("created_at").filter(coupon__is_available=True)
    serializer_class = CourseDetailSerializer
    pagination_class = CouponDetailPagination

    def get(self, request, *args, **kwargs):
        update_user_activity(request.user)
        return super().get(request, *args, **kwargs)
    
    def throttled(self, request, wait):
        wait = math.ceil(wait)
        raise Throttled(detail={
              "message":"request limit exceeded",
              "Retry-After":f"{wait} seconds"
        })
    


    
def home(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        token, _ = CustomToken.objects.get_or_create(user=user)
        context = {"token": token.key}
    return render(request, "home.html", context=context)

def dashboard(request):
    if not  request.user.is_authenticated:
        return render(request, "home.html")
    
    activities = UserDailyActivity.objects.filter(user=request.user).order_by('date')
    dates = [activity.date.strftime('%Y-%m-%d') for activity in activities]
    request_counts = [activity.request_count for activity in activities]

    active_coupons = Coupon.objects.filter(is_available=True).count()
    total_requests = UserDailyActivity.objects.filter(user=request.user).aggregate(Sum('request_count'))['request_count__sum'] or 0
    
    # Convert lists to JSON strings
    context = {
        'dates_json': json.dumps(dates),
        'request_counts_json': json.dumps(request_counts),
        'active_coupons': active_coupons,
        'total_requests': total_requests
    }
    return render(request, 'dashboard.html', context)
