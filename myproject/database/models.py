from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid




class Database(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, verbose_name="ID")
    name = models.CharField(max_length=200, verbose_name="パチモン名")  # パチモン名

    #初期値100 1以上 合計600以下になるように設定する。
    toughness_stats = models.IntegerField(default=100, verbose_name="基礎値(タフネス)")  # 基礎値(タフネス)
    power_stats = models.IntegerField(default=100, verbose_name="基礎値(パワー)")  # 基礎値(パワー)
    muscle_mass_stats = models.IntegerField(default=100, verbose_name="基礎値(筋肉量)")  # 基礎値(筋肉量)
    intelligence_stats = models.IntegerField(default=100, verbose_name="基礎値(賢さ)")  # 基礎値(賢さ)
    resistance_stats = models.IntegerField(default=100, verbose_name="基礎値(耐性)")  # 基礎値(耐性)
    speed_stats = models.IntegerField(default=100, verbose_name="基礎値(速度)")  # 基礎値(速度)

    #初期値0 0以上31以下
    toughness_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(タフネス)")  # タフネスセンス
    power_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(パワー)")  # パワーセンス
    muscle_mass_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(筋肉量)")  # 筋肉量センス
    intelligence_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(賢さ)")  # 賢さセンス
    resistance_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(耐性)")  # 耐性センス
    speed_sense = models.IntegerField(default=16, validators = [MinValueValidator(0), MaxValueValidator(31)], verbose_name="才能(速度)")  # 速度センス
    
    #初期値0 0以上256以下 合計が510になるように設定する。
    toughness_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(タフネス)")  # 努力指数(タフネス)
    power_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(パワー)")  # 努力指数(パワー)
    muscle_mass_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(筋肉量)")  # 努力指数(筋肉量)
    intelligence_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(賢さ)")  # 努力指数(賢さ)
    resistance_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(耐性)")  # 努力指数(耐性)
    speed_effort_value  = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(256)], verbose_name="努力指数(速度)")  # 努力指数(速度)
    
    #toughnessは (stats*2 + sense + effort_value) / 2 + 60
    #それ以外は (stats*2 + sense + effort_value) / 2
    toughness = models.IntegerField(default=0, verbose_name="実数値(タフネス)")  # 実数値(タフネス)
    power = models.IntegerField(default=0, verbose_name="実数値(パワー)")  # 実数値(パワー)
    muscle_mass = models.IntegerField(default=0, verbose_name="実数値(筋肉量)")  # 実数値(筋肉量)
    intelligence = models.IntegerField(default=0, verbose_name=" 実数値(賢さ)")  # 実数値(賢さ)
    resistance = models.IntegerField(default=0, verbose_name="実数値(耐性)")  # 実数値(耐性)
    speed = models.IntegerField(default=0, verbose_name="実数値(速度)")  # 実数値(速度)

    #charactar = models.CharField(max_length=10, verbose_name="センス") # センス
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    #実数値の計算
    def save(self, *args, **kwargs):
        self.toughness = (self.toughness_stats * 2 + self.toughness_sense + self.toughness_effort_value / 4) // 2 + 60
        self.power = (self.power_stats * 2 + self.power_sense + self.power_effort_value /4) // 2
        self.muscle_mass = (self.muscle_mass_stats * 2 + self.muscle_mass_sense + self.muscle_mass_effort_value / 4) // 2 + 5
        self.intelligence= (self.intelligence_stats * 2 + self.intelligence_sense + self.intelligence_effort_value / 4) // 2 + 5
        self.resistance = (self.resistance_stats * 2 + self.resistance_sense + self.resistance_effort_value / 4) // 2 + 5
        self.speed = (self.speed_stats * 2 + self.speed_sense + self.speed_effort_value /4 ) // 2 + 5
        super().save(*args, **kwargs)



    def __str__(self):
        return self.name

