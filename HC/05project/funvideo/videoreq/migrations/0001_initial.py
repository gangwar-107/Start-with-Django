# Generated by Django 2.2.1 on 2019-06-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videotitle', models.CharField(max_length=50)),
                ('videodesc', models.TextField()),
            ],
        ),
    ]