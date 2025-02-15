from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle

from .models import CourseDetail, Coupon

class CustomUserRateThrottle(UserRateThrottle):
    rate = '50/day'  # Custom rate for this endpoint


class CouponDetailPagination(PageNumberPagination):
  page_size = 5
  max_page_size = 50

class CouponSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coupon
    fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
  coupon = CouponSerializer()
  class Meta:
    model = CourseDetail
    fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
