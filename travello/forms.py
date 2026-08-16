from django import forms
from . models import Feedback, Comp_result
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

class Comp_resultForm(forms.ModelForm):
    class Meta:
        model = Comp_result
        fields = "__all__"