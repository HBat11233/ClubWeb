from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = ['enrollCode', 'enrollName', 'enrollGender',
                  'enrollCollege', 'enrollEmail', 'enrollIntro']
