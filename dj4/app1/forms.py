from django import forms
from app1.models import students
class inputweb(forms.ModelForm):
	class Meta:
		model=students
		fields=["name1"]