from django import forms
from .models import Resume
from .models import Drink

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['name','name_en','name_cat','desc','desc_en','desc_cat','price','category','file']
class DrinkForm(forms.ModelForm):

   class Meta:
      model = Drink
      fields = ['name','price','file']