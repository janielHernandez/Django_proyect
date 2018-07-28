from django import forms
from ..models import Contacter


class ContacterForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)
    subject = forms.CharField(max_length=100)


class ContacterModelForm(forms.ModelForm):
    class Meta:
        model = Contacter
        fields = ["name", "email", "subject"]

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if "@" not in data:
            raise forms.ValidationError("Su direccion de email no es valida")
        return data

    def clean_name(self):
        subject = self.cleaned_data.get("subject")
        if subject == "":
            return "Not Subject"
        return subject

