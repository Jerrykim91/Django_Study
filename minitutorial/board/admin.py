# board/admin.py
from django.contrib import admin
from.models import Article

# Register your models here.

# 어드민 사이트에 모델 등록
admin.site.register(Article)





# @admin.register(Article)  #  @admin.register(Article) 데코레이터로 wrapping => 상세한 설정가능

# class ArticleAdmin(admin.ModelAdmin):
#     # list_display => 문자열의 튜플로 저장 => admin 사이트의 리스트에서 튜플순 대로 테이블컬럼을 생성
#     list_display = ('id', 'title', 'author', 'date_created')  # date_created는 아래 정의한 메소드
#     list_display_links = ('id', 'title')                      # 상세페이지로 이동할 수 있는 필드 리스트
    # # 출력형식 변경 => %Y-%m-%d 형식으로 출력
#     def date_created(self, obj):                              # create_at 필드의 출력형식을 변경해주는 메소드
#         return obj.created_at.strftime("%Y-%m-%d")

#     date_created.admin_order_field = 'created_at'             # date_created 제목을 클릭시 선언 데이터 기준으로 정렬
#     date_created.short_description = '작성일'                 # date_created 컬럼 제목에 보일 텍스트