# Generated by Django 3.2.3 on 2021-06-06 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_author_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_add_article', 'Can add article'), ('can_manage_article', 'Can manage article')), 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
