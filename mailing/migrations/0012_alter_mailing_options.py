# Generated by Django 5.0.1 on 2024-01-28 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0011_alter_mailing_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('name_mailing',), 'permissions': [('can_blocked', 'can_blocked')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылка'},
        ),
    ]
