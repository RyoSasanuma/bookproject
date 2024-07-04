from django.db import models
from accounts.models import User

class Book(models.Model):
    id = models.AutoField(primary_key=True)                                 # 明示的にidフィールドを定義
    
    isbn_code = models.CharField(max_length=13, unique=True)                # ISVNコード[必須]
    title = models.CharField(max_length=200)                                # タイトル[必須]
    authors = models.CharField(max_length=200)                              # 著者[必須]　※リストで返ってくる
    publisher = models.CharField(max_length=200, blank=True, null=True)     # 出版社
    published_date = models.CharField(max_length=20, blank=True, null=True) # 出版日
    description = models.TextField(blank=True, null=True)                   # 書籍の説明
    page_count = models.IntegerField(blank=True, null=True)                 # ページ数
    categories = models.CharField(max_length=200, blank=True, null=True)    # 書籍のカテゴリー　※リストで返ってくる
    average_rating = models.FloatField(blank=True, null=True)               # 平均評価（1〜5の範囲）
    ratings_count = models.IntegerField(blank=True, null=True)              # 評価の件数
    small_thumbnail = models.URLField(blank=True, null=True)                # 小さいサムネイル画像のURL
    thumbnail = models.URLField(blank=True, null=True)                      # サムネイル画像のURL
    language = models.CharField(max_length=10, blank=True, null=True)       # 書籍の言語コード（ISO 639-1)[必須]

    date_add = models.DateTimeField(auto_now_add=True)                      # 登録日
    user = models.ForeignKey(User, on_delete=models.CASCADE)                # 登録ユーザー

    def __str__(self):
        return self.title
