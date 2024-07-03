"""
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)                     # 明示的にidフィールドを定義
    isbn_code = models.CharField(max_length=13, unique=True)    # ISVNコード
    title = models.CharField(max_length=200)                    # タイトル
    authors = models.CharField(max_length=200)                  # 著者　※リストで返ってくる
    publisher = models.CharField(max_length=200, blank=True, null=True)                                                # 出版社
    published_date = models.CharField(max_length=20)            # 出版日
    description = models.TextField(blank=True, null=True)                                               # 書籍の説明
    page_count = models.IntegerField(blank=True, null=True)                                               # ページ数
    categories = models.CharField(max_length=200, blank=True, null=True)                                                # 書籍のカテゴリー
    average_rating = models.FloatField(blank=True, null=True)                                          # 平均評価（1〜5の範囲）
    ratings_count = models.IntegerField(blank=True, null=True)                                            # 評価の件数
    small_thumbnail = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)                                               # 書籍の画像リンク
    language = models.CharField(max_length=10, blank=True, null=True)                                                 # 書籍の言語コード（ISO 639-1)




    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
"""