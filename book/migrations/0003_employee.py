# Generated by Django 4.0.1 on 2022-02-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]