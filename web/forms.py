from django import forms 
from multiupload.fields import MultiFileField

from web.models import Product, Images


class ProductForm(forms.ModelForm):
    section = forms.CharField(widget=forms.TextInput(attrs={'class': "input"}), label="Cloth Type (Comma separated)")

    class Meta:
        model= Product
        exclude = ("id","is_deleted","tags","published_date")

        widgets = {
            "title": forms.TextInput(attrs={'class':"input"}),
            "description": forms.TextInput(attrs={'class':"input"})
        }


class ImagesForm(forms.ModelForm):
    # images = forms.FileField(
    #     label="Image",
    #     widget=forms.ClearableFileInput(attrs={"multiple": True}),
    # )
    images = MultiFileField(min_num=1, max_num=10)

    class Meta:
        model = Images
        fields = ("images",)