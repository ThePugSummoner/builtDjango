# Generated by Django 4.2.2 on 2023-07-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_employee_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
