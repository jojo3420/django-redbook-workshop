from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import NameForm
from .models import ContactForm

def index(request):
    return render(request, 'form_example/index.html')


def your_name(request):
    if request.method == 'GET':
        # 빈 폼을 사용자에게 보여 준다.
        # unbound form 생성
        nameForm = NameForm()

    elif request.method == 'POST':
        # 클라이언트 submit 요청 처리
        # bound form 생성하기
        nameForm = NameForm(request.POST)
        # validation check
        # 폼 검증 결과가 False 이면 맨 아래의 render 가 실행되며 이전 입력한 폼데이터가 전달된다.
        if nameForm.is_valid():
            # form data 가 유효하면, 데이터는 cleaned_data 로 복사된다.
            new_your_name = nameForm.cleaned_data['your_name']
            print('new_your_name: ', new_your_name)
            # 추가 로직이 있으면 실행함...

            # form post 요청은 항상 redirect!
            return HttpResponseRedirect('thanks/')

    return render(request, 'form_example/name.html', {'nameForm': nameForm})


def thanks(request):
    return render(request, 'form_example/thanks.html')


def contact_form(request):
    global contact_form
    if request.method == 'GET':
        contact_form = ContactForm()

    elif request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            sender = contact_form.cleaned_data['sender']
            cc_myself = contact_form.cleaned_data['cc_myself']
            print('subject:', subject, ', message:', message, 'sender:', sender, ',cc_myself:', cc_myself)
            return HttpResponseRedirect(reverse('form_example:thanks'))

    return render(request, 'form_example/contact.html', {'contact_form': contact_form})