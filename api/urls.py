from django.urls import path
from api.views import CourseDetailListAPIView, GenerateTokenAPIView
 
urlpatterns = [
    path('courses/', CourseDetailListAPIView.as_view(), name='course-detail-list'),
    path('generate-token/', GenerateTokenAPIView.as_view(), name="generate-token"),
]