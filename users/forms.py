from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import CSVModel
User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email",max_length=100,widget=forms.EmailInput())
    first_name = forms.CharField(label='First Name',max_length=50,widget=forms.TextInput())
    last_name = forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name","last_name","username", "email")
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None


class CsvForm(ModelForm):
    phone_number = forms.RegexField(regex=r'^\+(?:\d\s?){7,15}$',label="Phone Number",required=False,widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 30, 'rows': 2}))
    first_name = forms.CharField(label="First Name",required=False,widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 30, 'rows': 2}))
    last_name = forms.CharField(label="Last Name",required=False,widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 30, 'rows': 2}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'style': 'width:280px;height:25px;margin-bottom:5px;font-size:15px'}),required=False)
    education = forms.CharField(label="Education",widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 60, 'rows': 10}),required=False)
    skills = forms.CharField(label="Skills",widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 60, 'rows': 10}),required=False)
    additional = forms.CharField(label="Additional",widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 60, 'rows': 10}),required=False)
    experience = forms.CharField(label="Experience",widget=forms.Textarea(attrs={'style': 'font-size: large','cols': 60, 'rows': 15}),required=False)
    class Meta:
        model = CSVModel
        fields = ['first_name', 'last_name', 'email', 'phone_number','experience','skills','education','additional']

    def __init__(self,*args, **kwargs):
        initial = kwargs.get('initial', {})
        super(ModelForm, self).__init__(*args, **kwargs)

    