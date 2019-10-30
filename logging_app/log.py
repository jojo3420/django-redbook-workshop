"""
default logging settings
    django 에서 로깅 설정 안할시 기본적으로 설정되어 있는 설정임.
"""
DEFAULT_LOGGING = {
    'version': 1,
    # dicConfig version 1 형식인데 현재는 버전이 하나뿐임.
    'disable_existing_loggers': False,
    # 기존의 로거들을 비활성화 하지 않음, 이전 버전과의 호환성을 위한 항목으로, 디폴트는 True임 (그러면 기존 로거들은 비활성화됨)
    # 비활성화의 의미지는 삭제하지는 않고 로깅 동작만 중시시킴,  장고에서는 이항목을 False 사용하도록 권장
    'filters': {
        # DEBUG=False 인 경우만 핸들러가 동작함
        # 특별키 () 의 의미는 필터 객체를 생성하기 위한 클래스를, 파이썬의 기본 클래스와는 다르게 장고에서 별도로 정의했다는것을 알려줌.
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # DEBUG=TRUE 인 경우만 핸들러 동작,
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        # 로그 생성 시각과 로그 메시지만들 출력 하도록 설정 , () 의 의미는 장고에서 별로로 포맷터를 정의 하였다는 뜻임.
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        # 'INFO' 레벨 및 그 이상의 메시지를 표훈 에러로 출력해주는 StreamHandler 클래스를 사용,
        # 이클래스는 require_debug_true 필터를 사용함.
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        # 'INFO' 레벨 및 그 이상의 메시지를 표훈 에러로 출력해주는 StreamHandler 클래스를 사용,
        # 이 핸들러는 django.server formatter 사용함
        # django.server.logger 에서 이 핸들러를 사용함
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server'
        },
        # ERROR 및 그 이상의 로그 메시지를 사이트 관리자에게 이메일로 보내주는 AdminEmailHandler 클래스 아용
        # require_debug_false 필터 사용
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        # 'INFO' 및 그 이상의 로그 메시지를 콜솔 밑 mail_admins 핸들러에게 보낸다.
        # django.* 계층 즉, django package의 촤상위 로거임
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        # 'INFO' 및 그 이상의 로그 메시지를 콜솔 밑 django.server 핸들러에게 보낸다.
        # 상위 로거로 로그 메시지를 전파하지 않음
        # 이 로거는 장고 개발 서버(runserver)에서 사용하는 로거임
        # 5XX 응답읕 ERROR 메시지로 4XX 응답은 WARNING 메시지로, 그외는 INFO 메시지로 출력
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


"""
 위 디폴트 설정 내욜을 보면 다음과 같은 사항을 알 수 있음
 만일 DEBUG=True 이면, django.* 계층에서 발생하는 로그 레코드는 INFO 레벨 이상일 때 콘솔로 보내진다. 
 만일 DEBUG=False 이면, django.* 계층에서 발생하는 로그 케로드는 ERROR 레벨 이상일 때 관리자에게 이메일 전송 된다.
 
 django.server logger는, DEBUG 값에 무관하게, 로그 레코드가 INFO 레벨 이상이면 콘솔로 보내짐.
 django.* 계층의 다른 로거들과는 다르게 django 로거로 전파하지 않음 
 
"""


"""
  <장고의 로깅 모듈 추가사항 정리> 
  
* 로거 *
 django 로거 :   앞에서 설명
        'INFO' 및 그 이상의 로그 메시지를 콜솔 밑 mail_admins 핸들러에게 보낸다.
        # django.* 계층 즉, django package 의 촤상위 로거임
        
 django.request 로거:  요청 처리와 관련된 메시지 기록, 5XX 응답은 ERROR 메시지로, 4XX응답은 WARNING 메시지 발생
  이 로거에 담기는 메시지는 2개의 추가적인 메타 항목 가짐 
    - status_code: HTTP 응답코드 
    - request: 로그 메시지를 생성하는 요청 객체 
    
  django.server 로거:    
         # 'INFO' 및 그 이상의 로그 메시지를 콜솔 밑 django.server 핸들러에게 보낸다.
        # 상위 로거로 로그 메시지를 전파하지 않음
        # 이 로거는 장고 개발 서버(runserver)에서 사용하는 로거임
        # 5XX 응답읕 ERROR 메시지로 4XX 응답은 WARNING 메시지로, 그외는 INFO 메시지로 출력


  django.template 로거:  template을 렌더링 하는 과정에서 발생하는 로그 메시지 기록 
    
  django.db.backends 로거:  데이터베이스 관련 로그메시지 기록
        예를 들어, 애플리케이션에서 사용하는 모든 SQL 문장들이 이로거에 DEBUG 레벨로 기록됨.
        이 로거에 담기는 메시지는 아래처럼 추가적인 메타 항목을 가짐.
        성능상의 이유로, SQL 로깅은 settings.DEBUG 항목이 True인 경우에만 활성화됨 
        
        - duration: SQL 문장을 실행하는데 걸린 시간 
        - sql: 실행된 SQL 문장 
        - params: SQL 호출에 사용된 파라미터 
        
        
  django.security.* 로거: 사용자가 보안 측명에서 해를 끼칠수 있는 동작을 실행한 경우, 이에 대한 메시지를 기록함.
    예를 들어, HTTP Host 헤더가 ALLOWED_HOSTS 에 없다면 장고는 400 응답을 리턴하고 에레 메시지가 django.security.DisallowedHost 로거에 기록됨 
    
  
  django.db.backends.schema 로거: 데이터베이스의 스키마 변경시 사용된 SQL 쿼리를 기록 
        
        
* 핸들러 *
  AdminEmailHandler : 디폴드 설정에서 설명함 
  
  
* 필터 * 
  CallBackFilter: 이 필터는 콜백 함수를 지정해서 필터를 통과하는 모든 메시지에 대해 콜백 함수를 호출 해줌.
        콜백 함수의 리턴값이 False 이면 메시지 로깅은 더 이상 진행하지 않음.
  
  RequireDebugFalse: 디폴트 설정 설명 
  
  RequireDebugTrue:  디폴트 설정 설명
  
"""