from django import forms
from django.core import validators
#Approach3 : using Custom/user defined validators:
def is_first_letter_capital(value):
    if value.istitle() != True:
        raise forms.ValidationError('First Letter should be capital')

class EmpSignInForm(forms.Form):
    fullname=forms.CharField(max_length=10,help_text='10 chracters max.')
    age=forms.IntegerField()
    # Approach2 : using Inbuilt Validators:
    city=forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(10)])
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput(),validators=[is_first_letter_capital])
    address=forms.CharField(widget=forms.Textarea)
    #Approach1 : Using Clean_fielname()
    def clean_fullname(self):
        print("Validating Fullname")
        fn = self.cleaned_data['fullname']
        if len(fn)<5:
            raise forms.ValidationError("Your name must be grater than 5 letters")
        return fn
    def clean_age(self):
        print('Validating age')
        age=self.cleaned_data['age']
        if age > 100:
            raise forms.ValidationError('Age must be less than 100')
        return age