from django.shortcuts import render
import logging

# settings.py 설정 파일에 정의한 로거를 취득함
# logger = logging.getLogger('my-logger')

# 로깅 호출ㅇ르 모듈단위로 계층화
logger = logging.getLogger('logging_app.logger')

"""
<로깅 모듈>
         4가지 주요 컴포넌트가 있다. => 로거, 핸들러, 필터, 포맷터
          요약 :  로거에 로그메시지가 쌓인다. 로그메세지의 로그레벨이 로거보다 높으면 핸들러에게 전해진다. 
                 핸들러에서 로그메시지를 파일로 저장할지, 표준 출력할지 결정한다. (1개의 로거에 n개의 핸들러 등록 가능)
                 로거에서 핸들러 전해질때 필터를 거친다.  => 포맷터 ==> 최종 출력
                 
         
         또한 장고의 runserver 나 웹서버에 의해 장고가 실행될 때 장고는 settings.py 파일에 정의된
         LOGGING_CONFIG, LOGGING 설정 항목을 참고하여 로깅관련 설정을 처리한다.
         settings.py에 관련 항목이 없으면 디폴트 로길 설정으로 시작됨.

        Logger: 로깅 시스템의 시작점,  로그 메시지를 처리하기 위해 메시지를 담아두는 저장소!

        파이썬 로그 레벨
        로그레벨  정수 값      설명
        NOTSET    0   로그 레벨의 최하위 수준, 로거 또는 핸들러가 생성될 때 별도 설정이 없으면 갖는 디폴드 로그레벨
        DEBUG    10   디버그 용도로 사용되는 정보
        INFO     20   일반적이고 보편적인 정보
        WARNNING 30   문제점 중에서 덜 중요한 문제점이 발생 시 이에 대한 정보
        ERROR    40   문제점 중에서 주요 문제점이 발생시 이에 대한 정보
        CRITICAL 50   치명적인 문제점이 발생 시 이에 대한 정보, (로그 레벨의 최상위 수준)

        로거에 저장되는 메시지를 로그 레코드라고 하며, 로그 레코드 역시 그 메시지의 심각성을 나타내는 로그레벨을 가진다.
        message가 logger 도달 하면  로그 레코드의 레벨과 로거 레벨 비교 한다.
        로그 레코드의 로그 레벨이 로거의 레벨보다 크거가 같으면 메시지 처리를 진행하고, 낮으면 메시지를 무시한다.
        이렇게 로그 레코드와 로거의 로그 레벨을 비교하여 메시지 처리를 진행하는것으로 결정되면
        로거는 메시지를 핸들러 에게 넘겨준다.

        *핸들러
        핸들러는 로거에 있는 메시지에 무슨 작업을 할지 결정하는 엔진이다.
        즉 메시지를 화면이나 파일 또는 네트워크 소켓들 어디에 기록할 것인지와 같은 로그의 동작을 정의함
        핸들러도 로거와 마찮가지로 로그 레벨을 가지고 있다.
        로그 레코드의 로그 레벨이 핸들러의 로그 레벨보다 낮으면 메시지를 무시한다.
        로거는 핸들러를 여러 개 가질 수 있고, 각 핸들러는 서로 다른 로그 레벨을 가질 수 있다.
        이렇게 해서 메시지의 중요도에 따라 다른 방식의 로그 처리가 가능
        ex) ERROR 또는 CRITICAL 메시지는 표준 출력으로 보내는 핸들러를 하나 만들고,
            차후 분석을 위해 이들 메시지를 파일에 기록하는 또 다른 핸들러 만들 수 있다.

      *필터
      로그 레코드(message)가 로거에서 핸들러로 넘겨질 때, 필터를 사용해서 로그 레코드에 추가적인 제어를 할수 있음
      기본 제어 방식은 로그 레벨을 지정하여 그 로그 레벨에 해당되면 괸련 로그 메시지를 처리 하는 것임
      그런데 필터를 추가 적용하면 로그 처리 기준을 추가 할 수 있게 된다.
      예를 들어, 필터를 추가하여 ERROR 메시지 중에서 특정 소스로부터 오는 메시지만 핸들러로 넘길 수 있다.
      필터를 사용하면 로그 레코드를 보내기전에 수정도 가능함.
      예를 들어 어떤 조건에 맞으면 ERROR 로그 레코드를 WARRING 로그 레벨로 낮춰주는 필터를 만들 수 도 있다.
      필터는 로거 또는 핸들러 양쪽에 적용이 가능하고, 여러개의 필터를 체인 방식으로 동작 시킬 수도 있음

      *포맷터
       로그레코드는 최종적으로 텍스트로 표현되는데, 포맷터는 표현시 사용할 포맷을 지정해줌.

      <로거 사용 및 로거 이름 계층화>
      로그를 기록하기 위해서는 설명한 로거, 핸들러, 필터, 포맷터 등을 설정한 후에, 코드 내에서 로깅 메소드를 호출
      settings.py gogo~



    <로거의 계층화>
    도트 방식의 로거 이름은 계층화를 이룬다. 
    즉 logging_app.view.my-logger 로거의 부모는 logging_app.view 이고 
    logging_app.view 의 부모는 logging_app 이며 파이썬 최상위 루트 로거는 getLogger('') 빈문자열 이다.
    로거의 계층과가 중요한 이유는 로깅 호출은  부모 로거에게 전파 되기 때문에 중요함.
    즉 로거 트리의 최상단 루트로거에서 핸들러 하나만을 만들어도 하위 로거의 모든 로깅 호출을 잡을 수 있다.
    이런 로깅 호출의 전파는 로거 단위로 제어할 수있는데, 특정 로거에서 상위 로거로 전파되는것을 비활성화 시킬 수 도 있음
     장고 로거 정리 
     1. django logger
     2. django.request logger : status_code, request 메타항목 가짐  
     3. django.server logger 
     4. django.template logger 
     5. django.db.backend logger : duration, sql, params 메타항목 가짐  
     6. django.security.* logger :   
     7. django.db.backends.schema logger
    
     필터 정리 
     1. CallbackFilter
     2. RequiredDebugFalse
     3. RequiredDebugTrue 
    """


def index(request):
    # DEBUG 레벨의 로그 레코드 출력
    logger.debug('현재 로그레벨은 info 이므로 아래레벨인 DEBUG 레벨의 로그 레코드는 출력되지 않음!')
    # INFO Level 로그 레코드 출력
    logger.info('info - logging_app.index')
    # WARNING LEVEL
    logger.warning('warning level')
    # ERROR 레벨의 로그 레코드를 출력
    logger.error('error - Something went wrong!')
    # CRITICAL LEVEL
    logger.critical('CRITICAL')
    # logger.log() : 원하는 로그 레벨을 정해서 로그 메시지 생성
    # logger.log(level='info', msg='hello world')
    # logging.exception() : 예외 스택 트레이스 정보를 포함하여 ERROR 레벨의 로그 메시지를 생성함
    return render(request, 'logging_app/index.html')
