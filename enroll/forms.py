from django import forms
from .models import enrollment

class enrollmentForm(forms.ModelForm):
    class Meta:
        model=enrollment
        fields = ['enrollCode','enrollName','enrollGender','enrollCollege','enrollEmail','enrollIntro']
