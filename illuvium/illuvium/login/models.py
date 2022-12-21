# モデル読込
from django.db import models

# コマンド
# python manage.py makemigrations login
# python manage.py migrate               



# モデルクラスを作成
class People(models.Model):
	# 項目定義
    Name     = models.CharField(max_length=50)           # 文字列
    # Tell     = models.IntegerField(blank=True, null=True) # 整数
    Mail     = models.EmailField(max_length=100)          # Email
    
    # テキスト表示
    def __str__(self):
    	return self.name