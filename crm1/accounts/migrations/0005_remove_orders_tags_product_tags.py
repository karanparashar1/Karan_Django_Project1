# Generated by Django 4.1.5 on 2023-01-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag_orders_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
