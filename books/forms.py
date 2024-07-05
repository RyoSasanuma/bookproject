from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'isbn_code',
            'title',
            'authors',
            'publisher', 
            'published_date', 
            'description', 
            'page_count', 
            'categories', 
            'average_rating', 
            'ratings_count', 
            'small_thumbnail', 
            'thumbnail', 
            'language'
            ]
        widgets = {
            'isbn_code': forms.TextInput(attrs={'readonly': 'readonly'}), 
        }




        """
        widgets 属性は、Djangoのフォームで使用されるウィジェットを指定するためのものです。
        ウィジェットは、フォームフィールドがどのようにレンダリングされるか（表示されるか）を制御します。
        具体的には、各フィールドに対してどのHTML要素（例：<input>、<textarea>など）を使用するか、
        そしてその要素に適用する属性（例：readonly、classなど）を指定できます。

        ■ widgets 属性の役割
          ● ウィジェットのカスタマイズ: フォームフィールドのデフォルトのレンダリング方法をカスタマイズします。
          ● HTML属性の設定: ウィジェットに追加のHTML属性を設定します（例：プレースホルダー、CSSクラス、読み取り専用など）。
        """