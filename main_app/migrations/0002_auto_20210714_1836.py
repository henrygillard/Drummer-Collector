# Generated by Django 3.2.3 on 2021-07-14 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drummer',
            name='cymbal_sponsor',
        ),
        migrations.RemoveField(
            model_name='drummer',
            name='drum_sponsor',
        ),
        migrations.RemoveField(
            model_name='drummer',
            name='head_sponsor',
        ),
        migrations.RemoveField(
            model_name='drummer',
            name='stick_sponsor',
        ),
        migrations.AlterField(
            model_name='drummer',
            name='band',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='drummer',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='drummer',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stick_sponsor', models.CharField(choices=[('V', 'Vic Firth'), ('P', 'ProMark'), ('I', 'Innovative Percussion')], default='None', max_length=1)),
                ('drummer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drummer')),
            ],
        ),
    ]