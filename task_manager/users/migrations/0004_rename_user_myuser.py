# Generated by Django 4.1.3 on 2022-11-10 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_nick_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
    ]