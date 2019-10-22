from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


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
    def get(self, request):
        print(request.method)
        return HttpResponse('GET result')

    def post(self, request):
        print(request.method)
        return HttpResponse('POST result')

    def put(self, request):
        print(request.method)
        return HttpResponse('put result')