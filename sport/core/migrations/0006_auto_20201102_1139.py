# Generated by Django 3.1.2 on 2020-11-02 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='username',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
    ]