from django.urls import path
from django.views.generic import TemplateView
from api.views import CourseDetailListAPIView, GenerateTokenAPIView
 
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
    path('courses/', CourseDetailListAPIView.as_view(), name='course-detail-list'),
    path('generate-token/', GenerateTokenAPIView.as_view(), name="generate-token"),
]