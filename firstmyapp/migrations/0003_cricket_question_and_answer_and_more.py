# Generated by Django 4.2 on 2023-05-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstmyapp', '0002_technologies_alter_mobile_technology_waves_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cricket_Question_and_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterModelTable(
            name='mobile_technology_waves',
            table='mobile_technology_waves',
        ),
        migrations.AlterModelTable(
            name='technologies',
            table='technologies',
        ),
    ]
