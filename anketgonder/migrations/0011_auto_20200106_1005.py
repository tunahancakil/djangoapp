# Generated by Django 2.2.7 on 2020-01-06 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '__first__'),
        ('anketgonder', '0010_auto_20200106_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cevaplar',
            name='anket_soru_id',
        ),
        migrations.AddField(
            model_name='cevaplar',
            name='anket_soru_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='anket.Sorular'),
        ),
    ]