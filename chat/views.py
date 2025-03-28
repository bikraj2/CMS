from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from courses.models import Course
# Create your views here.


@login_required 
def course_chat_room(request,course_id):
    try:
        course = request.user.course_joined.get(id=course_id)
    except Course.DoesNotExistError:
        return HttpResponseForbidden()
    return render(request,'chat/room.html',{'course':course})


