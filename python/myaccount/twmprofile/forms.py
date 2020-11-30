from django import forms
from django.core import validators

class SignupRequest(forms.Form):

    # creating our own custom validator
    def custom_username_validator(value):
        if(not 'gmail' in value):
            raise forms.ValidationError('Email must be end with @gmail.com')

    username = forms.EmailField(validators=[custom_username_validator])
    password = forms.CharField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    age = forms.IntegerField(required=False)
    comment = forms.CharField(required=False, label='Enter comment here', widget=forms.Textarea, validators=[validators.MaxLengthValidator(10)]) # emplicit validation
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    # Explicit validation for each field (must starts with clean_ followed by the field name)
    def clean_firstName(self):
        enteredfirstName = self.cleaned_data['firstName']
        if(not enteredfirstName.isalpha()):
            raise forms.ValidationError('firstName must not contain the numeric value')
        return enteredfirstName


    #Clean validation for all.This is mostly requried when you validate the re-enter of password
    def clean(self):
        print("Total form validation is being done.....")
        cleaned_data = super().clean()

        enteredbothandler = cleaned_data['bot_handler']
        if(len(enteredbothandler) > 0):
            raise forms.ValidationError('This form is submitted by a robot, could not be proceed.')

        enteredPassword = cleaned_data['password']
        if(len(enteredPassword) > 5):
            raise forms.ValidationError('Password length must not be greater than 5')

        print("Total form validation completed. Everything looks good.....")


