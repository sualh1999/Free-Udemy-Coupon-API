import uuid
from django.contrib.auth.models import User

from django.db import models

class Coupon(models.Model):
    coupon_str = models.CharField(max_length=255)
    is_available  = models.BooleanField(default=True)
    discount_deadline = models.CharField(max_length=255, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expires_at = models.CharField(max_length=255, null=True, blank=True)
    uses_remaining = models.IntegerField(null=True, blank=True)
    maximum_uses = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coupon_str or "Unavailable"


class CourseDetail(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image_link = models.URLField()
    description = models.TextField()
    link = models.URLField()
    video_content_length = models.CharField(max_length=50, null=True, blank=True)
    student_count = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    total_ratings = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    what_you_will_learn = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    big_description = models.TextField(null=True, blank=True)
    who_this_course_is_for = models.TextField(null=True, blank=True)
    coupon = models.OneToOneField(Coupon, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def generate_link(self):
        return self.link + "?couponCode=" + self.coupon.coupon_str
    
class CustomToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    key = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)
    
    def generate_key(self):
        return f"U-D-{uuid.uuid4().hex[:10].upper()}"
    
    def __str__(self):
        return self.key


