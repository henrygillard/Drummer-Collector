# Generated by Django 3.2.3 on 2021-07-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210714_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='stick_sponsor',
            field=models.CharField(choices=[('V', 'Vic Firth'), ('P', 'ProMark'), ('I', 'Innovative Percussion'), ('Z', 'Zildjian')], default='None', max_length=1),
        ),
    ]