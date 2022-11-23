from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path('', views.login, name='login'),
    path('mgr_login', views.login_mgr, name='mgr_login')
]