# Generated by Django 4.0.6 on 2022-07-09 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=128)),
                ('shipping_address', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=11)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('given_to_work', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('U', 'Unisex')], max_length=2)),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(upload_to='images')),
                ('image3', models.ImageField(upload_to='images')),
                ('image4', models.ImageField(blank=True, upload_to='images')),
                ('image5', models.ImageField(blank=True, upload_to='images')),
                ('image6', models.ImageField(blank=True, upload_to='images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizesSneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_34', models.PositiveIntegerField(default=0)),
                ('size_35', models.PositiveIntegerField(default=0)),
                ('size_36', models.PositiveIntegerField(default=0)),
                ('size_37', models.PositiveIntegerField(default=0)),
                ('size_38', models.PositiveIntegerField(default=0)),
                ('size_39', models.PositiveIntegerField(default=0)),
                ('size_40', models.PositiveIntegerField(default=0)),
                ('size_41', models.PositiveIntegerField(default=0)),
                ('size_42', models.PositiveIntegerField(default=0)),
                ('size_43', models.PositiveIntegerField(default=0)),
                ('size_44', models.PositiveIntegerField(default=0)),
                ('size_45', models.PositiveIntegerField(default=0)),
                ('sneaker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='store.sneaker')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sneaker_size', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='store.orderlist')),
                ('sneaker_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.sneaker')),
            ],
        ),
    ]