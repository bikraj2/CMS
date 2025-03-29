from django.shortcuts import get_object_or_404
from django.shortcuts import reverse,redirect
from .models import Course

def subdomain_course_middleware(get_response):
    def middleware(request):
        host_parts= request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0]!='www':
            course = get_object_or_404(Course,slug=host_parts[0])
            course_url = reverse('course_detail',args=[course.id])
            url = f'{request.scheme}://{".".join(host_parts[1:]),course_url}'
            return redirect(url)
        return get_response(request)
    return middleware
