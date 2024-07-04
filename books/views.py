
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required
def book_add(request):
    """
    books/book_form.html のフォーム入力データがPOSTされた場合は、
    ISBNコードをAPIに渡し、書籍データを取得してDBに保存する。
    その後、新規に登録した書籍データの詳細画面を表示する。
    """
    if request.method == 'POST':
        # book_form.html に入力されたISBNコードの取得
        isbn = request.POST.get('isbn')
        if isbn:
            response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
            data = response.json()
            # APIレスポンスデータに'items'データが存在した場合
            if 'items' in data:
                volume_info = data['items'][0]['volumeInfo']
                book = Book(
                    isbn_code=isbn,
                    title=volume_info.get('title', ''),
                    authors=', '.join(volume_info.get('authors', [])),
                    publisher=volume_info.get('publisher'),
                    published_date=volume_info.get('publishedDate'),
                    description=volume_info.get('description'),
                    page_count=volume_info.get('pageCount'),
                    categories=', '.join(volume_info.get('categories', [])),
                    average_rating=volume_info.get('averageRating'),
                    ratings_count=volume_info.get('ratingsCount'),
                    small_thumbnail=volume_info.get(['imageLinks']['smallThumbnail']),
                    thumbnail=volume_info.get(['imageLinks']['thumbnail'])
                    language=volume_info.get('language'),
                    user=request.user,  
                )
                book.save()
                return redirect('book_list')
            
        # APIからデータ(items)が取得できなかった場合は・・・これは何をしている？
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        """
        urlsからの直接ルーティングの場合は、ISBNコード入力フォームを表示する。
        """
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

    





# トップページ (テスト用の暫定関数)
def top(request):
    return render(request, "books/top.html")