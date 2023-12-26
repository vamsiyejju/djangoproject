from django.forms import ModelForm, TextInput
from .models import climate

class climateform(ModelForm):
    class Meta:
        model = climate
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'enter city'}),
        } 