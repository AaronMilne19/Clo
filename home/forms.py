from django import forms
from django.contrib.auth.models import User
from home.models import Magazine, UserProfile, MagazineIssue, Hashtag, UserProfile



class UserForm(forms.ModelForm):
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
	password =forms.CharField(required=True,min_length=8, widget=forms.widgets.PasswordInput())
	confirm_password =forms.CharField(required=True, widget=forms.widgets.PasswordInput())

	
	class Meta:
		model=User
		fields=('email','username','password')
		
	def clean(self):
		cleaned_data=super(UserForm, self).clean()
		password=self.cleaned_data.get("password")
		confirm_password=self.cleaned_data.get("confirm_password")

		if password!=confirm_password:
			self.add_error("confirm_password","Passwords do not match.")
			
		return cleaned_data

	#def clean_email(self):
#		cleaned_data = super(UserForm, self).clean()
#		email = self.cleaned_data.get("email")
#		if User.objects.filter(email=email).exists():
#			self.add_error("email", "Account with this email already exists")
#			#raise ValidationError("Email exists")
#		return cleaned_data
	
	
class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=()

class UploadCodesFileForm(forms.Form):
	amount = forms.IntegerField(required=True, min_value=1, max_value=500, widget=forms.widgets.NumberInput)