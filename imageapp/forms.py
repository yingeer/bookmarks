from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "url", "description",)
        widgets = {
            "title": forms.CharField(widget=forms.Textarea),
            "url": forms.HiddenInput,
        }
        labels = {
            "url": "link",
        }

        