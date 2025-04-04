from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form to add or edit a product."""

    class Meta:
        model = Product
        fields = '__all__'
       
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        catetegories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in catetegories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            