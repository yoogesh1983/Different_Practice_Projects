from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.forms import DateInput
from YMSBlog.models import Profile

"""
class SignupRequest(forms.ModelForm):

    # creating our own custom validator
    def custom_username_validator(value):
        if(not 'gmail' in value):
            raise forms.ValidationError('Email must be end with @gmail.com')

    username = forms.EmailField(validators=[custom_username_validator])
    password = forms.CharField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    age = forms.IntegerField(required=False)
    comment = forms.CharField(required=False, label='Enter comment here', widget=forms.Textarea, validators=[validators.MaxLengthValidator(20)]) # emplicit validation
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    #release_date = forms.DateField(widget=DateInput(attrs={'class': 'yms'}))
    #director_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile

        # I want all fields present inside model
        fields = '__all__'

        # I want to specify what to save in db, This means for age it will take the default of 18 since we have defined 18 in Profile model
        # Remember this is a tuple
        #fields = ('username', 'password', 'firstName', 'lastName')

        # I want to save all except these fields
        # Remember this is a list
        #exclude = ['firstName', 'lastName']



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
        if(len(enteredPassword) > 10):
            raise forms.ValidationError('Password length must not be greater than 10')

        enteredAge = self.cleaned_data['age']
        if enteredAge is None:
            raise forms.ValidationError('Age must be required.')

        print("Total form validation completed. Everything looks good.....")

class ProfileUpdateRequest(forms.ModelForm):
    class Meta:
        model = Profile

        # Remember this is a tuple
        fields = ('username', 'password', 'firstName', 'lastName', 'age')

class AdminSignupRequest(forms.ModelForm):
    class Meta:
        model = User

        # I want to specify what to save in db, This means for age it will take the default of 18 since we have defined 18 in Profile model
        # Remember this is a tuple
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

"""

