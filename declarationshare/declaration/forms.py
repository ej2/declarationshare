from django import forms
from django.forms import model_to_dict

from declarationshare.declaration.models import Declaration


class DeclarationForm(forms.Form):
    text = forms.CharField(max_length=255, widget=forms.TextInput())
    anonymous = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    author = forms.CharField(max_length=50, widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop("user")
        #self.declare_type = kwargs.pop("declare_type")
        self.instance = kwargs.pop("instance", None)

        super(DeclarationForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.initial = model_to_dict(self.instance)

    @property
    def is_edit(self):
        return self.instance is not None

    def save(self):
        data = self.cleaned_data

        if self.instance:
            declaration = self.instance
        else:
            declaration = Declaration()

        declaration.text = data.get("text")
        declaration.anonymous = data.get("anonymous")
        declaration.author = data.get("author")
        #declaration.type = self.declare_type

        declaration.save()

        return declaration
