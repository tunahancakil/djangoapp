# Generated by Django 2.2.7 on 2020-01-06 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anketgonder', '0011_auto_20200106_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='anket_soru_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='anket.Sorular'),
        ),
    ]