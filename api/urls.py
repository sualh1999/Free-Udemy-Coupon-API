from django.urls import path
from django.views.generic import TemplateView
from api import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('docs/', TemplateView.as_view(template_name="docs.html")),
    path('api/courses/', views.CourseDetailListAPIView.as_view(), name='course-detail-list'),
]