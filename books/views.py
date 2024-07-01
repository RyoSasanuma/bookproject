from django.shortcuts import render, redirect

# トップページ (テスト用の暫定関数)
def top(request):
    return render(request, "books/top.html")