from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from accountapp.models import BookInfo
from .models import Book

# 호출 당시에 현재 요청에 모든 내역을 인자로 전달 받음
def book_list(request):
    qs = BookInfo.objects.all().order_by('-public_year')
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    # render의 첫번째 인자는 view 함수의 request인자를 그대로 넘겨줌
    # 두번째 인자는 템플릿명
    # 세번째 인자로 dictionary로 qs라는 값을 참조할텐데 참조할 이름 지정
    return render(request, 'book/book_list.html', {
        'book_list' : qs,
        'q' : q
    })


def book_detail(request, isbn):
    book = BookInfo.objects.get(isbn=isbn)
    return render(request, 'book/book_info.html', {'book':book})