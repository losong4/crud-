# Generated by Django 3.2.2 on 2021-06-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default='닉네임을 입력해주세요', max_length=15),
        ),
    ]
