# Generated by Django 3.2.4 on 2021-07-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='F1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('category_type', models.IntegerField(blank=True, null=True)),
                ('question', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
