# board/migrations/0002_auto_20200119_0206.py
# Generated by Django 2.2.5 on 2020-01-19 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]
    # 오타 수정 
    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]