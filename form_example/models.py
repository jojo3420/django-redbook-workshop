# from django.db import models
from django import forms


class NameForm(forms.Form):
    # max_length 용도
    # 1> html input 엘리먼트에 maxlength="100" 효과
    # 2> form data validation check
    your_name = forms.CharField(label='Your Name', max_length=10) # default widget=Forms.TextInput
    # CharFiled default 위젯은 TextInput 클래스이며  이 위젯은 <input type='text'> tag 와 대응 된다.
    # 다른 위젯으로 변경하려면... your_name = forms.CharField(label='your name', max_length=100, widget=Forms.TextArea)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label='email')
    cc_myself = forms.BooleanField(required=False)





