from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class CustomerCreationForm(UserCreationForm):
    fname = forms.CharField(max_length=50, label='Nombre', required=True)
    lname1 = forms.CharField(max_length=50, label='Apellido Paterno', required=True)
    lname2 = forms.CharField(max_length=50, label='Apellido Materno', required=True)
    rut = forms.CharField(max_length=50, label='Rut', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    confirm_email = forms.EmailField(label='Confirmar E-mail', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_confirm_email(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')

        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Los correos electrónicos no coinciden.")
        
        return confirm_email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['fname']
        user.last_name = self.cleaned_data['lname1'] + ' ' + self.cleaned_data['lname2']
        if commit:
            user.save()
            customer = Customer.objects.create(
                user=user,
                fname=self.cleaned_data['fname'],
                lname1=self.cleaned_data['lname1'],
                lname2=self.cleaned_data['lname2'],
                rut=self.cleaned_data['rut']
            )
        return user

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fname', 'lname1', 'lname2', 'rut']
        labels = {
            'fname': 'Nombre',
            'lname1': 'Apellido Paterno',
            'lname2': 'Apellido Materno',
            'rut': 'RUT',
        }