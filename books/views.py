from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book
from books.models import Author
from books.models import Publisher


class BooksModelView(TemplateView):
    """
        TemplateView 특징
            - 특별한 로직이 없고 템플릿(html) 파일만 렌더링 할경우 TemplateView 상속 받음
            - template_name 클래스 변수 오버라이딩!
            - 템플릿으로 넘겨 줄 컨텍스트 변수가 있을 경우에는 부모의 get_context_data() 메서드를 오버라이딩 해준다.

    """
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


class BookList(ListView):
    """
        ListView 특징
        객체가 들어 있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿 계층에 넘겨 주면 된다.
        만일 이런 리스트를 테이블에 들어있는 모든 레코드를 가져와 구성하는 경우 테이블명,
        즉 모델 클래스명만 지정해주면 된다.

        그리고 명식적으로 지정하지 않아도 장고에서 디폴트로 지정해주는 속성이 2가지 있음
        1> 컨텍스트 변수명으로 "object_list" 사용하며 템플릿에서 사용하면 됨.
        2> 템플릿 파일을 모델명소문자_list.hrml 형식의 이름으로 지정됨
            ex) book_list.html , author_list.html , publisher_list.html
    """
    # Book table 의 모든 레코드를 가져와 object_list 라는 컨텍스트 변수에 할당함
    # 템플릿 파일은 books/book_list.html 이 됨
    model = Book


class BookDetail(DetailView):
    """
        DetailView 특징
        특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 계층에 넘겨 준다.
        만일 테이블에서 PK로 조회해서 특정 객체를 가져오는 경우에는 테이블명, 즉 모델 클래스명만 지정해주면 된다.
        조회시 사용할 PK 값은 URLconf 에서 추출해서 사용함

        장고에서 디폴트로 지정된 속성 2가지
        1> context 변수명으로 "object" 사용
        2> 템플릿 이름으로 모델명소문자_detail.html 형식이 됨
    """
    # Book 테이블에서 pk로 필터링 한후 컨텍스트 변수 "object"에 할당시킴 , 그리고 books/book_list.html 리턴됨
    model = Book


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class PublisherDetail(DetailView):
    model = Publisher

