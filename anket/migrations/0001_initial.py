# Generated by Django 2.2.7 on 2020-02-18 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurumlar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unvan', models.CharField(max_length=250, verbose_name='İş Yeri Ünvanı')),
                ('iletisim_no', models.CharField(max_length=10, verbose_name='İletişim No')),
                ('email', models.EmailField(max_length=50)),
                ('puan', models.IntegerField(default=0)),
                ('islem_tarihi', models.DateTimeField()),
                ('kullanici_adi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sorular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('soru_baslik', models.CharField(max_length=250, verbose_name='Soru Grubu')),
                ('soru_icerik', models.TextField(verbose_name='Soru İçerik')),
                ('islem_tarihi', models.DateTimeField(auto_now_add=True)),
                ('kullanici_adi', models.CharField(max_length=50, verbose_name='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Yoneticiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=50, verbose_name='Yönetici Ad')),
                ('soyad', models.CharField(max_length=50, verbose_name='Yönetici Soyad')),
                ('email', models.EmailField(max_length=50)),
                ('iletisim_no', models.CharField(max_length=10, verbose_name='İletişim No')),
                ('kurum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anket.Kurumlar')),
            ],
        ),
        migrations.CreateModel(
            name='Isciler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=50, verbose_name='Ad')),
                ('soyad', models.CharField(max_length=50, verbose_name='Soyad')),
                ('email', models.EmailField(max_length=50)),
                ('iletisim_no', models.CharField(max_length=10, verbose_name='İletişim No')),
                ('islem_tarihi', models.DateField(auto_now_add=True)),
                ('yonetici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anket.Yoneticiler')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
