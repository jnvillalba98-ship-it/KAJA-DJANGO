from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            "codigo",
            "nombre",
            "descripcion",
            "precio",
            "stock",
        ]

        widgets = {

            "codigo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el código del producto"
                }
            ),

            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del producto"
                }
            ),

            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Descripción del producto"
                }
            ),

            "precio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el precio"
                }
            ),

            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el stock"
                }
            ),
        }