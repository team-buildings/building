# Generated by Django 5.0.6 on 2024-08-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_clients_oylik_tolov_home_square_home_total_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='term',
            field=models.CharField(choices=[('---', '---'), (5, '5 yil'), (6, '6 yil'), (7, '7 yil'), (8, '8 yil'), (9, '9 yil'), (10, '10 yil'), (11, '11 yil'), (12, '13 yil'), (14, '14 yil'), (15, '15 yil'), (16, '16 yil'), (17, '17 yil'), (18, '18 yil'), (19, '19 yil'), (20, '20 yil')], default='---', max_length=50, verbose_name="To'lov muddati"),
        ),
    ]
