#########################
# Author:      Nate Cao
# Version:     1.0
# since:       2020-07-24
# last-modify: 2020-07-24
#########################
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class IndexForm(forms.Form):
    """
    IndexForm class defines the fields of index.html. Use the local and global hook functions to
    validate the fields
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'email', 'name': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'name': 'username'}, render_value=True),
                               min_length=9,
                               error_messages={'min_length': "Password must be longer than 8 characters."})

    colourChoices = [
        ('', 'Choose colour'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('black', 'Black'),
        ('brown', 'Brown'),
    ]
    animalChoices = [
        ('bear', 'Bear'),
        ('tiger', 'Tiger'),
        ('snake', 'Snake'),
        ('donkey', 'Donkey'),
    ]
    colour = forms.ChoiceField(widget=forms.Select(attrs={'id' : 'colour', 'name': 'colour'}),
                               choices=colourChoices,
                               required=True)
    animal = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       choices=animalChoices)
    tiger_type = forms.CharField(widget=forms.TextInput(attrs={'name': 'tiger_type', 'id': 'tiger_type'}),
                                 required=False)

    def clean_email(self):
        """
        Local hook function to validate the format of email. Otherwise a ValidationError would be raised.

        @return: email of clean data
        @rtype: str
        """
        val = self.cleaned_data.get('email')

        validate_email(val)
        return val

    def clean_animal(self):
        """
        Local hook function to validate at least two animals would be chosen. Otherwise raise a
        ValidationError.

        @return: the chosen animals
        @rtype: List
        """
        val = self.cleaned_data.get('animal')
        if len(val) < 2:
            raise ValidationError("At least two Animals must be chosen.")
        else:
            return val

    def clean(self):
        """
        Global hook function to validate when tiger is chosen in animal, the input field of the type of tiger
        is required. Otherwise a ValidationError would be raised

        @return: clean data
        @rtype: dict
        """
        animals = self.cleaned_data.get('animal')
        val = self.cleaned_data.get('tiger_type')
        if animals:
            if 'tiger' in animals:
                if val == '':
                    raise ValidationError("Type of tiger is required.")
                else:
                    return self.cleaned_data
        return self.cleaned_data




