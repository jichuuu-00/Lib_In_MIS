from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book'), # 함수 그 자체를 넘기는 것으로 호출 안되게 해야함
    path('<int:pk>', views.book_detail, name='searchbook'),
]