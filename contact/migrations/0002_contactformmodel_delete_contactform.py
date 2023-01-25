# Generated by Django 4.1.5 on 2023-01-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
