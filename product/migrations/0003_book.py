# Generated by Django 5.0.1 on 2024-01-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_desctiption_alter_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('author', models.TextField()),
            ],
        ),
    ]