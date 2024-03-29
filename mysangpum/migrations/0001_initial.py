# Generated by Django 2.2.7 on 2019-11-18 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('maker_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysangpum.Maker')),
            ],
        ),
    ]
