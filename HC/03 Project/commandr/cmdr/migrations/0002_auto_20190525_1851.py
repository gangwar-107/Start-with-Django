# Generated by Django 2.2.1 on 2019-05-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='cmdr',
        ),
    ]