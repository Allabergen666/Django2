# Generated by Django 4.2.1 on 2023-05-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('subjectname', models.CharField(max_length=50, verbose_name='Subject name')),
                ('lengthofservice', models.CharField(max_length=50, verbose_name='Length of service')),
            ],
            options={
                'verbose_name': 'Teachers',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студенты'},
        ),
    ]