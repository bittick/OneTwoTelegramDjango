# Generated by Django 4.0.6 on 2022-07-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО клиента')),
                ('telegram_id', models.CharField(max_length=15, verbose_name='Telegram id')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image1', models.ImageField(upload_to='images', verbose_name='Фото')),
                ('weight', models.CharField(choices=[('G', 'грамм'), ('KG', 'килограмм')], max_length=2, verbose_name='Еденица измерения массы')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=6, null=True, unique=True, verbose_name='Номер заказа')),
                ('shipping_address', models.CharField(max_length=128, verbose_name='Адрес доставки')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплата совершена')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store_vegetables.customer', verbose_name='ФИО клиента')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='store_vegetables.orderlist')),
                ('vegetable_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store_vegetables.vegetable', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Список товаров',
                'verbose_name_plural': 'Список товаров',
            },
        ),
    ]
