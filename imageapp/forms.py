from django import forms
from .models import Image
from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile


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
            
    def save(self, commit=True):
        """把写在视图函数里的方法写在forms里面，避免复用"""
        # image已经是一个对象了
        image_obj = super().save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = "{}.{}".format(slugify(image_obj.title), image_url.split(".")[-1])
        response = request.urlopne(image_url)
        # 下面的关于image存储 ????
        image_obj.image.save(image_name, ContentFile(response.read()))
        if commit:
            image_obj.save()
        else: 
            return image_obj