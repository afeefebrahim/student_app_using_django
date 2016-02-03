from django import forms
from student_app.models import student,UserProfile
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
        #exclude = ['picture']
        
class studentForm(forms.ModelForm):
	name = forms.CharField(max_length=128,help_text="Enter the name")
	sex = forms.CharField(max_length=128 ,help_text="Enter the sex")
	age = forms.IntegerField(help_text="Enter the age")
	mark = forms.IntegerField(help_text="Enter the mark")
	class Meta:
		model = student
		fields = ('name','sex','age','mark')

