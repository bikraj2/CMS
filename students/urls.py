from django.urls import path
from django.views.decorators.cache import cache_page
from students.views import StudenRegistrationView, StudentCourseDetailView, StudentCourseListView, StudentEnrollCourseView
urlpatterns = [
    path('register',view=StudenRegistrationView.as_view(),name = 'student_registration'),
    path('enroll-course',view=StudentEnrollCourseView.as_view(),name = 'student_enroll_course'),
    path('courses/',view=StudentCourseListView.as_view(),name='student_course_list'),
    path('courses/<pk>',view=cache_page(60*15)(StudentCourseDetailView.as_view()),name='student_course_detail'),
    path('courses/<pk>/<module_id>/',view=StudentCourseDetailView.as_view(),name='student_course_detail_module'),
]
