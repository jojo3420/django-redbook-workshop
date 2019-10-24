from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import FormView
from .models import Book
from .form import MyForm


def index(request):
    return render(request, 'class_view/index.html')


class MyClassView(View):
    """
     class-based view
     상속 과 믹스인 기능을 사용해 코드 재사용 가능.(중복 제거)
     제너릭 뷰 역시 클래스 형 뷰

     상속받은 django.views.generic.View 에 dispath(), as_view() 메서드가 정의 되어 있음.

     클래스 뷰의 장점 2가지
        1. GET, POST method 분리 가능 (request.method == 'GET' 제거 가능)
        2. 다중상속과 같은 객체 지향 기술이 가능함.
           클래스형 제네릭 뷰 및 믹스인 클래스 등을 사용 할 수 있고, 이는 코드의 재사용성을 높여준다. (중복제거)
    """

    # 메서드 이름을 http Method 명으로 정의 하면 get 요청 처리가능
    # ==> View.dispatch() 메서드가 요청을 분석한 후 중계해줌
    def get(self, request):
        print(request.method)
        return HttpResponse('GET result')

    def post(self, request):
        print(request.method)
        return HttpResponse('POST result')

    def put(self, request):
        print(request.method)
        return HttpResponse('put result')


class BookListView(ListView):
    """
    클래스 뷰는 GET, POST 외에 HTTP Method 처리 가능

    HEAD method 사용: 서점에 방문한 직후에 새롭게 출간된 책이 있는지를 서버에게 문의하는 용도
       최근 발간된 책이 없는데도 책 리스트 전체 데이터를 서버로부터 받아온다면, 네트워크 대역폭 낭비이므로,
       신규 출간책이 있는 경우에만 응답. (이런 요청을 할때 Http HEAD Method 사용)
       HTTP 프로토콜 규격에 따르면 HEAD 요청에 대한 응답은 바디없이 헤더만 보내주면 된다.
   :param request:
   :return:
   """
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M%S GMT')
        return response


class AboutView(TemplateView):
    """
        <제네릭 뷰>
        단순 반복작업을 줄여 주기 위해 상속기능을 이용하여 장고에서 제공해주는 템플릿 뷰
        즉 제네릭 뷰란, 뷰 개발 과정에서 공통적으로 사용 할 수 있는 기능들을 추상화하고,
        이를 장고에서 미리 만들어  제공해주는 클래스형 뷰 이다.
        => 클래스 형 뷰를 선언 할 때 대부분 제너릭 뷰를 상속 받아서 작성하는것이 대부분임.
    """
    # 오버라이딩
    template_name = 'class_view/about.html'

    # => template view 는 뷰에 특별한 로직이 없고,
    # 이 샘플코드는 URL에 맞춰 해당 템플릿(html) 을 보여줄 때 사용하는 제네릭 뷰 임


"""
    제네릭 뷰 4가지 분류 
    1. Base View : view class를 생성하고, 다른 제네릭 뷰의 부모 클래스를 제공하는 기본 제네릭 뷰 
        종류 : View, TemplateView, RedirectView 
        View : 가장 기본이 되는 최상위 제네릭 뷰로 다른 모 든 제네릭 뷰는 View 의 하위 클래스 임
        TemplateView : 템플릿이 주어지면 템플릿을 렌더링 해줌 
        RedirectView: URL 이 주어지면 해당 URL로 리다이렉트 시켜줌 
        
    2. Generic Display View : 객체의 리스트를 보여주거나, 특정 객체의 상세 정보를 보여줌.
        종류 : ListView, DetailView 
        ListView :  조건에 맞는 여러 개의 객체를 보여줌 
        DetailView : 객체 하나에 대한 상세 정보를 보여줌 
    
    3. Generic Edit View : form 을 통해 객체를 생성, 수정, 삭제 하는 기능 제공
        종류 : FormView, CreateView, UpdateView, DeleteView 
        FormView : 폼이 주어지면 해당 폼을 보여준다.
        CreateView : 객체를 생성하는 폼을 보여준다. 
        UpdateView : 기존 객체를 수정하는 폼을 보여준다. 
        DeleteView : 기존 객체를 삭제하는 폼을 보여준다.
     
    4. Generic Date View : 날짜 기반 객체의 년/월/일 페이지로 구분해서 보여줌
        종류 : ArchiveIndexView, YearArchiveView, MonthArchiveView,
             WeekArchiveView, DayArchiveView, TodayArchiveView, DateDetailView 
              
         ArchiveIndexView : 조건에 맞는 여러 개의 객체 및 그 객체들에 대한 날짜 정보를 보여 줌 
         YearArchiveView : 연도가 주어지면 그 연도에 해당하는 객체들을 보여 줌  
         MonthArchiveView : 년, 월이 주어지면 그에 해당하는 객체들을 보여 줌 
         WeekArchiveView : 년도와 주차(week)가 주어지면 그애 해당하는 객체를 보여 줌 
         DayArchiveView : 년, 월, 일 이 주어지면 그 날짜에 해당하는 객체들을 보여줌 
         TodayArchiveView : 오늘 날짜에 해당하는 객체들을 보여줌 
         DateDetailView  : 년, 월, 일, 기본키(또는 슬러그)가 주어지면 그에 해당하는 특정 객체 하나에 대한 상세 정보 보여줌
"""


# function view VS class view
def my_function_view(request):
    if request.method == 'GET':
        # GET 처리
        form = MyForm(initial={'key': 'value'})

    elif request.method == 'POST':
        print('function-view post response..')
        form = MyForm(request.POST)
        if form.is_valid():
            # POST 응답처리 - 유효성 검증 통과
            # cleaned_data 로 로직 처리
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            email = form.cleaned_data['email']
            y_n = form.cleaned_data['y_n']
            print(title, subject, date, email, y_n)
            return HttpResponseRedirect('/class_view/success/')

    # GET: 정상응답 OR POST 유효성 실패 응답 처리
    return render(request, 'class_view/form_template.html', {'form': form})


# 제네릭 최상위 View 클래스를 상속 받음. 추후에 FormView 상속해서 처리하는 것도 나올 것임
class MyFormGenericView(View):
    """
    클래스형 뷰에서 폼 처리 패턴
    1> GET 요청에 대한 응답 => 템플릿 렌더링 하여 template 다시 보여줌
    2> Form POST 처리 => 유효성 패스 될 경우  데이터 처리 및 리다이렉트
    3> Form 유효성 검증 실패 POST : 에러 출력 및 template 다시 보여줌
    """
    # from 처리를 위해 폼 클래스를 오버라딩 해준다.
    form_class = MyForm
    # 폼 초기값 지정
    initial = {'key:', 'value'}
    # 템플릿 경로 지정
    template_name = 'class_view/form_template.html'

    def get(self, request, *args, **kwargs):
        # empty form template return
        form = self.form_class()  # form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # form POST 요청 처리
        print('form-class-view post response..')
        form = self.form_class(request.POST)
        if form.is_valid():
            # cleaned_data 로 관련 로직 처리
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            email = form.cleaned_data['email']
            y_n = form.cleaned_data['y_n']
            print(title, subject, date, email, y_n)
            return HttpResponseRedirect('/class_view/success/')

        # POST 유효성 실패 응답 처리
        return render(request, self.template_name, {'form': form})


# FormView 상속한 예제 코드
class MyFormView(FormView):
    """
        Generic FormView
         FormView 를 사용 하면 상위 FormView 클래스에서
         get(), post() 메서드의 처리가 정의 되어 있으므로 생략 가능.
         (POST 요청의 구체적 비지니스 로직은 어디서 처리 하는 거지?)

         주의할 점
            from_class : 사용자에게 보여줄 폼을 정의한 form.py 파일 내의 클래스명 => form.py로 분리 해야하나? OK
            template_name : 폼을 포함하여 렌더링할 템플릿 파일이름(html)
            success_url :  처리가 정상적으로 완료 되었을 때 리다이렉트 시킬 URL
            form_valid() 함수 : 폼 데이터 유효성 체크를 처리할 로직
                            super() 함수를 사용하면 success_url로 지정된 URL로 리다이렉트 처리됨
    """
    form_class = MyForm
    template_name = 'class_view/form_template.html'
    success_url = '/class_view/success/'

    def form_valid(self, form):
        # cleaned_data 관련 로직 처리
        title = form.cleaned_data['title']
        subject = form.cleaned_data['subject']
        date = form.cleaned_data['date']
        email = form.cleaned_data['email']
        y_n = form.cleaned_data['y_n']
        print(title, subject, date, email, y_n)
        # 부모클래스의 success_url 로 리다이렉트
        return super(MyFormView, self).form_valid(form)
