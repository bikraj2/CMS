from django.urls import  include, path
from rest_framework import routers
from courses.api.views import   CourseViewSet ,SubjectViewSet
app_name = 'courses'
router = routers.DefaultRouter()
router.register('courses',CourseViewSet)
router.register('subjects',SubjectViewSet)
urlpatterns = [
    path('',include(router.urls))
]
