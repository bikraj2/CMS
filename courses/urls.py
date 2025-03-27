from .views import ContentCreateUpdateView, ContentDeleteView, ContentOrderView, CourseDetailView, CourseListView, CourseModuleUpdateView, ManageCourseListView,CourseDeleteView,CourseUpdateView,CourseCreateView, ModuleContentListView, ModuleOrderView
from django.urls import path
# app_name = 'course'
urlpatterns =  [
    path('mine/',view=ManageCourseListView.as_view(),name='manage_course_list'),
    path('create/',view=CourseCreateView.as_view(),name='course_create'),
    path('<pk>/edit/',view=CourseUpdateView.as_view(),name='course_edit'),
    path('<pk>/delete/',view=CourseDeleteView.as_view(),name='course_delete'),
    path('<pk>/module/',view=CourseModuleUpdateView.as_view(),name='course_module_update'),
    path('module/<int:module_id>/',view=ModuleContentListView.as_view(),name='module_content_list'),
    path('content/<int:id>/delete',view=ContentDeleteView.as_view(),name='module_content_delete'),
    path('module/<int:module_id>/content/<model_name>/create/',view=ContentCreateUpdateView.as_view(),name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',view=ContentCreateUpdateView.as_view(),name='module_content_update'),
    path('module/order/',view=ModuleOrderView.as_view(),name='module_order'),
    path('content/order/',view=ContentOrderView.as_view(),name='content_order'),
    path('subject/<slug:subject>/',view=CourseListView.as_view(),name='course_list_subject'),
    path('<slug:slug>/',view=CourseDetailView.as_view(),name='course_detail')
]

