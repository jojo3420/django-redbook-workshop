from django.shortcuts import render
import logging


# settings.py 설정 파일에 정의한 로거를 취득함
# logger = logging.getLogger('my-logger')

# 로깅 호출ㅇ르 모듈단위로 계층화
logger = logging.getLogger('logging_app.views.my-logger')
"""
로거의 계층화
도트 방식의 로거 이름은 계층화를 이룬다. 
즉 logging_app.view.my-logger 로거의 부모는 logging_app.view 이고 
logging_app.view 의 부모는 logging_app 이며 파이썬 최상위 루트 로거는 getLogger('') 빈문자열 이다.
로거의 계층과가 중요한 이유는 로깅 호출은  부모 로거에게 전파 되기 때문에 중요함.
즉 로거 트리의 최상단 루트로거에서 핸들러 하나만을 만들어도 하위 로거의 모든 로깅 호출을 잡을 수 있다.
이런 로깅 호출의 전파는 로거 단위로 제어할 수있는데, 특정 로거에서 상위 로거로 전파되는것을 비활성화 시킬 수 도 잇음
"""


def index(request):
    """
     파이썬 로그 레벨
            로그레벨  정수 값      설명
            NOTSET    0   로그 레벨의 최하위 수준, 로거 또는 핸들러가 생성될 때 별도 설정이 없으면 갖는 디폴드 로그레벨
            DEBUG    10   디버그 용도로 사용되는 정보
            INFO     20   일반적이고 보편적인 정보
            WARNING 30   문제점 중에서 덜 중요한 문제점이 발생 시 이에 대한 정보
            ERROR    40   문제점 중에서 주요 문제점이 발생시 이에 대한 정보
            CRITICAL 50   치명적인 문제점이 발생 시 이에 대한 정보, (로그 레벨의 최상위 수준)
    """

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
    #logger.log() : 원하는 로그 레벨을 정해서 로그 메시지 생성
    # logger.log(level='info', msg='hello world')
    #logging.exception() : 예외 스택 트레이스 정보를 포함하여 ERROR 레벨의 로그 메시지를 생성함
    return render(request, 'logging_app/index.html')
