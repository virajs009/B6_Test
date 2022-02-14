import datetime

from django import forms

from book.models import Book, Employee


# class StudentForm(forms.Form):                    # forms in django
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
#     password = forms.CharField(widget=forms.PasswordInput())

class StudentForm(forms.ModelForm):                 # model form - to use with available model as it is
    is_published = forms.BooleanField()
    choose_book_cover = forms.FileField()
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("is_active",)                    # must pass in tuple format


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=100)
    email = forms.EmailField(label='Enter your email', max_length=100)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("is_active",)

class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

