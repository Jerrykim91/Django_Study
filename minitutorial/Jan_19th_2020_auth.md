# 1차 작업(2020.01.18)
---

# 작업할당 
    => 회원 관리 시스템 + 뼈대 생성    

- 일단**auth프레임워크**부터 알아야 할것같음     
    => 작업을 진행하기전에 auth 개념 정리부터 

1. 새로운 모델 정의 
- 기본적으로 게시판이 구현이되면 누구나 작성하고 누구나 읽을 수 있다    
    + 그리고 어퓨징을 하는 사용자들을 제한하고 싶어 할것    
> 이럴때 접속자들에게 어떠한 이름을 부여 => 이름의 여부에 따라 기능을 제한가능 => **사용자 인증**     


## 장고의 auth framwork
- **가입 , 로그인 , 로그아웃 세가지 기능을 제공** 
- id 와 비밀번호를 포함한 모든 사용자 정보는 데이터 베이스에 기록 
- 로그인시 입력한 id와 비밀번호가 해당 id의 사용자와 동일한지를 판단   
- 


### 사용자 인증
- 사용자정보를 데이터베이스에 저장하고, 저장된 데이터를 구분할 수 있는 유일한 키를 지정해서 사용자를 식별하는 기능     
- 가입의 핵심 기능은 => 사용자를 구분할 수 있는 키를 사용자로부터 얻어오고 이것이 중복되지 않게 하는것       
- 비밀번호는 암호화해서 해당 웹사이트에서만 알아볼수있게 하거나 **해칭함수**를 통해서 원래의 비밀번호를 알아볼 수 없게 만들어 저장     


### 암호화 방법 
- 대부분의 웹사이트는 비밀번호를 해칭함수를 통해 원래의 비밀번호를 알아 낼수 없도록 저장          
    - 해시 함수=> 원래의 비밀번호를 알아볼 수 없게 저장   

> 암호화와 해시의 공통점      
    - 원래의 텍스트를 알아볼 수 없는 텍스트로 변경     
> 암호화와 해시의 차이점      
    - 암호화는 암호문에서 평문으로 돌릴수있지만 해시는 불가능 함     

### 이해를 위한 AbstractUser 클래스 코드

```py
# test-venv-36/lib/python3.6/site-packages/django/contrib/auth/models.py
# AbstractUser 클래스 
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    #username
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    #first_name
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    #
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    #
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    #date_joined
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True # makemigrations 커맨드 실행시에 무시

    # Meta 클래스 => outer 클래스의 옵션을 설정
    #   => 주로 ordering, indexes, unique_together, index_together 
    # ordering   => 검색시 기본 정렬 기준 
    # indexes    => 메모리 과소비/ 데이터베이스에서 빠르게 검색
    # unique_together => 데이터 중복 방지 
    # index_together => 데이터 베이스에 인덱스 생성 => 두개 이상의 필드 정의 

    # full_name
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
    # 이메일 전송 기능
    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

# User 클래스  
#   => AbstractUser를 상속받아 정의
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


# 여러종류의 사용자 모델이 필요하다면 AbstractUser를 상속받아 사용

```

### 커스텀 사용자 모델
AbstractUser => 필요한 기능만 있는것이 아님 
- 한국인은 first_name과 last_name 불필요
- 수정과 변경이 하고싶은 필드가 존재  => 식별자로 username이아니라 email을 사용  

- AbstractUser를 사용하지않고 커스터마이징을 해봄
    1. 먼저 사용자 앱을 생성 ``` ./manage.py startapp user```


```py

# 프로젝트이름/user/models.py

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# 코드시작----

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    name = models.CharField('이름', max_length=30, blank=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()
    # email을 사용자의 식별자로 설정
    USERNAME_FIELD = 'email'    
    # 필수입력값                 
    REQUIRED_FIELDS = ['name']                   

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)


# ======= 프로젝트이름/settings.py========

# 생략

INSTALLED_APPS = [
    'user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 생략

# AUTH_USER_MODEL 추가
AUTH_USER_MODEL = '앱label.모델명'           

```  

- 마이그레이션 진행      
    => ```manage.py makemigrations 어플이름```    

- 에러 발생할수 있음 
https://swarf00.github.io/2018/12/07/registration.html 참조
=> 이전에 생성했던 디비에서 생긴문제 NO PROBLEM

- 에러 발생 
    - 빈 데이터베이스에 admin 앱과 ABC 앱이 같이 마이그레이션 되어서 문제가 없었는데, 이미 admin 앱이 마이그레이션 된 상태에서 커스텀 유저 모델을 마이그레이션 하려니 문제가 되는 상황      
    => 해결방법은 admin 앱을 비활성화 시키면 됩니다. 커스텀 사용자 모델을 마이그레이션할 동안만 비활성화 =>  settings.py      



```py
# 모든 사용자 생성 메소드에 username 필드가 필수로 정의되어 있는데 username 파라미터는 사용하지 않으니 삭제
# user/models.py

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# 생략
```


```py
# admin 사이트에 새로운 사용자모델을 추가
# user/admin.py

from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'joined_at', 'last_login_at', 'is_superuser', 'is_active')
    list_display_links = ('id', 'email')
     # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음
    exclude = ('password',)                          

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    # 가장 최근에 가입한 사람부터 리스팅
    joined_at.admin_order_field = '-date_joined'      
    joined_at.short_description = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'
```
- 기본 사용자 정보 모델의 정의는 완료

## 이제 가입, 로그인, 로그아웃 구현 

### 회원가입 뷰 생성 
- 이미 회원가입능 위한 모델은 만들어져있음     
- 먼저 뷰 부터 구현     
    - TemplateView 대신 CreateView 를 이용할 예정    
    - CreateView 은 TemplateView 보다 많은 믹스인들이 추가되어 훨씬 다양한 기능들을 제공   
    - 이 기능들을 모두 사용하려면 규칙에 따라 설정해야 할 것들이 몇가지 있음     

```py
# user/views.py

from django.views.generic import CreateView
from user.models import User


class UserRegistrationView(CreateView):
    model = User                            # 자동생성 폼에서 사용할 모델
    # 장고에서 기본으로 생성되는 모델폼을 사용할 경우만 필요
    fields = ('email', 'name', 'password')  # 자동생성 폼에서 사용할 필드

# 모델폼 객체가 자동으로 생성될 때 참조하는 모델의 모든 필드를 폼의 필드로서 생성하지 않고 
# 필요한 필드들만 생성시켜야 하는데 이 때 fields 라는 클래스변수가 꼭 폼에서 생성시켜야 하는 모델의 필드명


# user/views.py

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from user.models import User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm




```
- TemplateView를 상속받아 정의하던 때랑 달라진 부분이 크게 model, fields 클래스변수가 추가
    - template_name 이라는 클래스변수가 사라진 점


```py
# minitutorial/urls.py

from django.contrib import admin
from django.urls import path

from bbs.views import hello, ArticleListView, ArticleDetailView, ArticleCreateUpdateView
from user.views import UserRegistrationView

urlpatterns = [
    path('hello/<to>', hello), 

    path('article/', ArticleListView.as_view()),
    path('article/create/', ArticleCreateUpdateView.as_view()),
    path('article/<article_id>/', ArticleDetailView.as_view()),
    path('article/<article_id>/update/', ArticleCreateUpdateView.as_view()),

    path('user/create/', UserRegistrationView.as_view()),

    path('admin/', admin.site.urls),
]

```



## 내가 구현해야할 기능  => 세션없이 진행 

### 사용자 인증시 필요한것들
    - 계정 id
    - 비번 pw
    - 생일(6자리) birth
    - 이메일
    - 성별(추후)

