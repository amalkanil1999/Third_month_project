# Generated by Django 4.2.7 on 2023-11-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
        migrations.RenameField(
            model_name='images',
            old_name='secondary_image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
