from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['name','name_en','desc','desc_en','price','category','file']