# Generated by Django 4.2.7 on 2023-11-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_blog_body_alter_blog_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.TextField(max_length=2000),
        ),
    ]
