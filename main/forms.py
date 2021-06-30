from django import forms


class addnewrequirement(forms.Form):
    Gender = [('male', 'Male'), ('female', 'Female'),
              ('transgender', 'TransGender'), ('other', 'Other')]
    BLOOD_GROUP = [('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),
                   ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')]

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    gender = forms.CharField(
        label='Gender', widget=forms.Select(choices=Gender, attrs={'class': 'form-control'}))
    blood_type = forms.CharField(
        label='Blood Group', widget=forms.Select(choices=BLOOD_GROUP, attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Number'}))
    hospital = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Hospital Name'}))
    address = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control', 'placeholder': 'Enter Full Address'}))
