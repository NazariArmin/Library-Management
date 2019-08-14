# Generated by Django 2.1.7 on 2019-08-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('published_date', models.DateField()),
            ],
        ),
    ]
