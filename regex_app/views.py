# regex_app/views.py
from django.shortcuts import render
import re

def confirm(request):
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        name = request.POST.get('name')
        age = request.POST.get('age')
        zip_code = request.POST.get('zip-code')
        tel = request.POST.get('tel')

        # 正規表現でのチェック
        name = re.sub(r'\s', '', name)  # スペースを除去

        error_messages = []

        # ageが半角数字のみかチェック
        if not re.match(r'^\d+$', age):
            error_messages.append('年齢は半角数字のみ入力してください')

        # zip_codeが半角数字と半角ハイフンのみかチェック
        if not re.match(r'^\d{3}-?\d{4}$', zip_code):
            error_messages.append('郵便番号は半角数字と半角ハイフンのみ入力してください')

        # telが半角数字と半角ハイフンのみかチェック
        if not re.match(r'^\d{2,5}-?\d{1,4}-?\d{4}$', tel):
            error_messages.append('電話番号は半角数字と半角ハイフンのみ入力してください')

        # エラーがあればindex.htmlにエラーメッセージと入力値を渡して遷移
        if error_messages:
            return render(request, 'regex_app/index.html', {'error_messages': error_messages, 'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})

        # すべての項目が正規表現にマッチした場合はconfirm.htmlに遷移
        return render(request, 'regex_app/confirm.html', {'name': name, 'age': age, 'zip_code': zip_code, 'tel': tel})

    # GETリクエストの場合はindex.htmlを表示
    return render(request, 'regex_app/index.html')
