# モデル読込
from django.db import models

# コマンド
# python manage.py makemigrations illuviumsite
# python manage.py migrate              

# migrationの履歴削除
# python manage.py migrate --fake illuviumsite zero 

# tier = [("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),]
# stage = [("1","1"),("2","2"),("3","3"),]
# モデルクラスを作成
class RateSearch(models.Model):
	# 項目定義
    IlluvialTier     = models.IntegerField(verbose_name="IlluvialTier")
    IlluvialStage    = models.IntegerField(verbose_name="IlluvialStage")
    ShardTier     = models.IntegerField(verbose_name="ShardTier")
    Captured     = models.BooleanField(verbose_name="捕獲成否")
    RegisterDate     = models.CharField(max_length=8)
    
    # テキスト表示
    def __str__(self):
    	return self.name
        