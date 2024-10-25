from django import forms
from .models import vehicle


# creating a form
class VehicleForm(forms.ModelForm):
    
    # create meta class
    class Meta:
        # specify model to be used
        model= vehicle

 #specify fields to be used
        fields = [
            "placa",
            "marca",
            "modelo",
            "color_vehiculo"
        ]

        labels= {
            'placa': 'Número de placa',
            'marca': 'Marca del vehículo',
            'modelo': 'Modelo del vehículo',
            'color_vehiculo': 'Color del vehículo'
        }
        
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }
        