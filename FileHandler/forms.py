from django import forms

class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes'
)
    docfile.widget.attrs.update({'type':'file', 'class':'custom-file-input', 'id' : 'inputGroupFile02'})
