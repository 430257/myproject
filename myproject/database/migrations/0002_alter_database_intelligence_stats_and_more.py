# Generated by Django 5.1.5 on 2025-02-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='intelligence_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(賢さ)'),
        ),
        migrations.AlterField(
            model_name='database',
            name='muscle_mass_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(筋肉量)'),
        ),
        migrations.AlterField(
            model_name='database',
            name='power_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(パワー)'),
        ),
        migrations.AlterField(
            model_name='database',
            name='resistance_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(耐性)'),
        ),
        migrations.AlterField(
            model_name='database',
            name='speed_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(速度)'),
        ),
        migrations.AlterField(
            model_name='database',
            name='toughness_stats',
            field=models.IntegerField(default=100, verbose_name='基礎値(タフネス)'),
        ),
    ]
