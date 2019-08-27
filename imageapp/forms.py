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

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extension = ["jpg", "jpeg"]
        cur_extension = url.split(".")[-1]
        if cur_extension not in valid_extension:
            raise forms.ValidationError("The given URL does not ' \
                                   'match valid image extensions.")
        
        return url
            
        