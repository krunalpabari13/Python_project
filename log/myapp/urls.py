from django.urls import path
from . import views
from . import apis
#every page name and roots
urlpatterns = [
    path('',views.index,name="indexpage"),
    path('checking', views.checking, name='checking'),
    # path('sign',views.sign,name="signup_back"),
    # path('login',views.login,name="signup_back"),
    path('auth-login-basic',views.auth_login_basic,name='log_front'),
    path('auth-register-basic',views.auth_register_basic,name='log_front'),
    path('data',views.data,name='data'),
    path('selected',apis.selected,name="sources"),
    path('login',apis.login,name='login'),
    path('sign',apis.sign,name='sign')
]