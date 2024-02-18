from django import forms
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام کاربری را وارد کنید'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'ایمیل را وارد کنید'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام را وارد کنید'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی را وارد کنید'}))
    password_1 = forms.CharField(max_length=50, widget=(forms.TextInput(attrs={'placeholder':'پسورد را وارد کنید'})))
    password_2 = forms.CharField(max_length=50, widget=(forms.TextInput(attrs={'placeholder':'تکرار پسورد را وارد کنید'})))

