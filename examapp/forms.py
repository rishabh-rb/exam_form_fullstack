from django import forms

from .models import ExamFormSubmission


class ExamFormSubmissionForm(forms.ModelForm):
    class Meta:
        model = ExamFormSubmission
        fields = ['full_name', 'course', 'year', 'address', 'phone_number']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
