from django.db import models
import uuid



class Database(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, verbose_name="ID")
    name = models.CharField(max_length=200, verbose_name="パチモン名")  # パチモン名
    toughness = models.IntegerField(verbose_name="タフネス")  # タフネス
    power = models.IntegerField(verbose_name="パワー")  # パワー
    hardness = models.IntegerField(verbose_name="硬さ")  # 硬さ
    intelligence = models.IntegerField(verbose_name="賢さ")  # 賢さ
    resistance = models.IntegerField(verbose_name="耐性")  # 耐性
    speed = models.IntegerField(verbose_name="速度")  # 速度
    power_sense = models.IntegerField(verbose_name="才能(パワー)")  # パワーセンス
    hardness_sense = models.IntegerField(verbose_name="才能(硬さ)")  # 硬さセンス
    intelligence_sense = models.IntegerField(verbose_name="才能(賢さ)")  # 賢さセンス
    resistance = models.IntegerField(verbose_name="才能(耐性)")  # 耐性センス
    speed = models.IntegerField(verbose_name="才能(速度)")  # 速度センス
    charactar = models.CharField(max_length=10, verbose_name="センス") # センス
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")


    def __str__(self):
        return self.name

