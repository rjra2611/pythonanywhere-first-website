# Generated by Django 3.1.1 on 2020-10-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='data',
            new_name='date',
        ),
    ]
