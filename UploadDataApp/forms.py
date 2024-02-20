from django import forms
from django.core.validators import FileExtensionValidator


class UploadDataForm(forms.Form):
    file = forms.FileField(
        label='Upload CSV File',
        validators=[FileExtensionValidator(['csv'])]
    )
