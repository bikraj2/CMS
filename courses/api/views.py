from django.views.generic import detail
from rest_framework.decorators import action, permission_classes
from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import  IsAuthenticated 
from courses.api import serializers
from courses.api.pagination import StandardPagination
from courses.api.permissions import IsEnrolled
from courses.api.serializers import CourseSerializer, CourseWithContentSerializer, SubjectSerializer
from courses.models import Course, Subject

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.prefetch_related('modules')
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination
    @action(detail=True,methods=['post'],authentication_classes=[BasicAuthentication],permission_classes=[IsAuthenticated])
    def enroll(self,request,*args,**kwargs):
        course  = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled':True})
    @action(detail=True,methods=['POST'],serializer_class =  CourseWithContentSerializer ,authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated,IsEnrolled])
    def contents(self,request,*args,**kwargs):
        return self.retrieve(request,*args,*kwargs)

