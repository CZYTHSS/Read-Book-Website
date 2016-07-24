from django import forms
 
class AddUserForm(forms.Form):
	user_name = forms.CharField(max_length=100 ,label='user_name')
	user_password = forms.CharField(max_length=100 ,label='user_password')