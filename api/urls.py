from django.urls import path
from django.views.generic import TemplateView
from api import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('docs/', TemplateView.as_view(template_name="docs.html")),
    path("explore/", views.ExploreView.as_view(), name="explore"),
    path('explore/<int:course_id>/', views.CourseDetailView.as_view(), name='course-detail'),
    path("search/", views.CourseSearchView.as_view(), name="search"),
    path('api/courses/', views.CourseDetailListAPIView.as_view(), name='course-detail-list'),
    path('api/courses/<int:pk>/', views.CourseDetailRetrieveAPIView.as_view(), name='course-detail'),

]