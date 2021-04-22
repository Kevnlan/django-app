from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Building, BuildingTenant
from bootstrap_datepicker_plus import DatePickerInput


class SignUpForm(UserCreationForm):
    phone = forms.IntegerField()
    name = forms.CharField(max_length=150)
    next_of_kin = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class BuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        exclude = ("owner", "tenant",)

class BuildingTenantForm(forms.ModelForm):

    class Meta:
        model = BuildingTenant
        fields = "__all__"
        widgets = {
            'checkInDate': DatePickerInput(), # default date-format %m/%d/%Y will be used
        }