# 패키지 
- django.shortcuts 
    - render()
        : 주어진 템플릿을 주어진 컨텍스트 사전과 결합 =>  HttpResponse렌더링 된 텍스트 가있는 객체를 반환
        **필수 인수**
        request : 응답을 생성하는데 사용 된 요청 객체 
        template_name : 사용할 템플리트의 전체 이름
        - render( **request** , **template_name** , context = None , content_type = None , status = None , using = None ) 

    - redirect()
        : HttpResponseRedirect전달 된 인수에  **URL을 반환**
