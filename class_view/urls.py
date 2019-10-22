from django.urls import path
# 함수 형 뷰 사용
from . import views

# Class 형 뷰 사용
from .views import MyClassView


app_name = 'class_view'
urlpatterns = [
    path('', views.index, name='index'),

    # 장고의 URL 해석기는 요청과 관련된 파라미터들을 클래스가 아니라 함수에 전달 하기 때문에,
    # 클래스형 뷰는 클래스로 진입하기 위한 as_view() 클래스 메소드를 제공한다.
    # as_view() 를 진입 메소드 라고도 한다. 이 메소드의 역할은 클래스의 인스턴스를 생성하고
    # 그 인스턴스의 dispatch() 메서드를 호출한다.
    # dispatch() 메서드는 요청을 검사해서 GET, POST 등의 HTTP Method 를 알아낸 다음
    # 인스턴스 내에서 해당 이름을 갖는 메서드로 요청을 중계 해준다.
    # 만약 해당 메서드가 없으면 HttpResponseNotAllow 예외를 발생시킴
    path('about/', MyClassView.as_view())
]
