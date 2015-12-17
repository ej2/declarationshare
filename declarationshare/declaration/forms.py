from django import forms
from django.forms import model_to_dict
from ipware.ip import get_ip

from declarationshare.declaration.models import Declaration


class DeclarationForm(forms.Form):
    text = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-element form-control"}))
    anonymous = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": " inputcheckbox"}))
    nsfw = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": " inputcheckbox"}))
    author = forms.CharField(
        required=False, max_length=35, widget=forms.TextInput(attrs={"class": "form-element form-control"}))

    def __init__(self, *args, **kwargs):
        self.declare_type = kwargs.pop("declare_type")
        self.instance = kwargs.pop("instance", None)
        self.request = kwargs.pop('request', None)

        super(DeclarationForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.initial = model_to_dict(self.instance)

    @property
    def is_edit(self):
        return self.instance is not None

    def clean_text(self):
        text = self.cleaned_data.get("text")

        if self.declare_type == 'WILL':
            text = text.replace("I will", "", 1)

        if self.declare_type == 'AM':
            text = text.replace("I am", "", 1)

        return text

    def save(self):
        data = self.cleaned_data

        if self.instance:
            declaration = self.instance
        else:
            declaration = Declaration()

        declaration.text = data.get("text")
        declaration.anonymous = data.get("anonymous")
        declaration.nsfw = data.get("nsfw")
        declaration.ip_address = get_ip(self.request)

        if data.get("author"):
            declaration.author = data.get("author")
        else:
            declaration.anonymous = True

        declaration.type = self.declare_type
        declaration.save()

        return declaration
