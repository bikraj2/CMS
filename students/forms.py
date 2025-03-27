from django import forms

from courses.models import Course


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput
    )
    def __init__(self,*args,**kwargs):
        super(CourseEnrollForm,self).__init__(*args,**kwargs)
