import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

""" 登録図書リスト一覧画面表示（TOPページ） """
@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/book_list.html', {'books': books})

""" ISBNコード入力による図書情報取得"""
@login_required
def fetch_book(request):
    if request.method == 'POST':
        isbn = request.POST['isbn']
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                volume_info = data['items'][0]['volumeInfo']
                form = BookForm(initial={
                    'isbn_code': isbn,
                    'title': volume_info.get('title', ''),
                    'authors': ', '.join(volume_info.get('authors', [])),
                    'publisher': volume_info.get('publisher'),
                    'published_date': volume_info.get('publishedDate'),
                    'description': volume_info.get('description'),
                    'page_count': volume_info.get('pageCount'),
                    'categories': ', '.join(volume_info.get('categories', [])),
                    'average_rating': volume_info.get('averageRating'),
                    'ratings_count': volume_info.get('ratingsCount'),
                    'small_thumbnail': volume_info.get('imageLinks', {}).get('smallThumbnail', ''), # 辞書型の多重構造の中からのデータ取得理解が浅い
                    'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                    'language': volume_info.get('language')
                })
                return render(request, 'books/book_form.html', {'form': form})
        else:
            # エラーハンドリング
            return render(request, 'books/fetch_book.html', {'error': 'Book not found'})
    return render(request, 'books/fetch_book.html')

""" ISBNフェッチ情報登録処理 """
@login_required
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('list')
        
    return render(request, 'books/book_form.html', {'error': 'エラー'})

""" 既存登録済図書情報編集処理 """
@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

""" 既存登録済図書情報削除処理 """
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})