# Generated by Django 4.0.1 on 2022-01-19 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_item_restaurant_item_user_menu_restaurant_menu_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='user',
        ),
    ]
