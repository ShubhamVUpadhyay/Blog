# Generated by Django 3.2.7 on 2023-09-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_authorizationrequest_blogpost_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='authorizationrequest',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='authorizationrequest',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
