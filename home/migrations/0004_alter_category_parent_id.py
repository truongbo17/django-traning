# Generated by Django 4.1.5 on 2023-01-27 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_category_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
