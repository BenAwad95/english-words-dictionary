# Generated by Django 3.0.7 on 2022-10-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theNewStore', '0009_auto_20210323_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmodel',
            name='pron_word_link',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Pronunciation link of word'),
        ),
    ]