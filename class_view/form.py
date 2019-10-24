from django import forms


class MyForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    subject = forms.CharField(max_length=500, widget=forms.Textarea)
    date = forms.DateTimeField()
    email = forms.EmailField()
    y_n = forms.BooleanField(required=False)