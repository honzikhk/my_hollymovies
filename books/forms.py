from django import forms
from books.models import Book, Author


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class BookForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput)

    class Meta:
        model = Book
        #fields = '__all__'         # not nessesary
        exclude = ['likes', ]       # there must be either exclude or fields


class AuthorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Author
        fields = '__all__'          # there must be either exclude or fields


