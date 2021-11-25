from django import forms
from .models import UserBooking


class BookingForm(forms.ModelForm):
    class Meta:
        model = UserBooking
        fields = ('full_name', 'email', 'number_of_people',
                  'phone_number', 'date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'number_of_people': 'Number of people',
            'phone_number': 'Phone Number',
            'date': 'date',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
