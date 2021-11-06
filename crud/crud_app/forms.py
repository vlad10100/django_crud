
from django import forms
from .models import Car

class Car_form(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('car_brand', 'car_model', 'car_color', 'car_classification')
        labels = {
            'car_brand': 'Brand',
            'car_model': 'Model',
            'car_color': 'Color',
            'car_classification': 'Classification'
        }


    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['car_classification'].empty_label = 'Car Classification'

