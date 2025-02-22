from django.contrib import admin
from .models import Coupon, CourseDetail, CustomToken, UserDailyActivity

admin.site.register(CustomToken)
admin.site.register(UserDailyActivity)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_str', 'discount_price', 'original_price', 'expires_at', 'updated_at']


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'title', 'student_count', 'rating', 'created_at', 'language']
