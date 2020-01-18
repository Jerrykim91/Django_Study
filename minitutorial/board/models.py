#board/models.py
from django.db import models

# Create your models here.

# 모델 설계전 구상 
# 1. 게시판 글 목록 나열
# 2. 제목과 작성자 표시 
# 3. 게시글 들어가면=> 상세화면으로 이동 => 제목 내용 작성일 출력
# 4. 상세화면에서 글 수정하기 클릭 => 글수정페이지로 이동 
# 5. 수정화면에서 저장하기 클릭 =>  수정된 내용이 저장 => 게시판으로 이동 
# 6. 수정화면에서 게시글 삭제 클릭 => 게시글이삭제 게시판으로 이동 
# 7. 새글작성 클릭 => 새로운 글쓰기화면출력 
# 8. 글 작성후 저장클릭 => 수정내용 저장후 게시판이동 


# 모델이름(Article)
# 속성 
# 제목(title), 내용(content), 작성자(author), 작성일(created_at)

class Article(models.Model):
    # 제목(title)
    title      = models.CharField('제목', max_length=126, null=False)
    # 내용(content)
    content    = models.TextField('내용', null=False)
    # 작성자(author)
    author     = models.CharField('작성자', max_length=16, null=False)
    # 작성일(created_at)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    # created_at.editable = True   # created의 editable 속성에 True를 설정 => 디테일하게 설정가능

# 자주 디버깅해야 할 오브젝트인데 매번 string formatter를 이용하는게 불편
#  그래서 모델에 __str__메소드를 오버라이드 함
def __str__(self):
    return '[{}] {}'.format(self.id, self.title)