from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Fields in contact form
    class Meta:
        fields = ['from_email', 'subject', 'message']

    # Placeholders in contact form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'from_email': 'Email',
            'subject': 'Subject',
            'message': 'How can we help?',
        }

        self.fields['from_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholder
