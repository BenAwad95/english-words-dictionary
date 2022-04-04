# Generated by Django 3.1.3 on 2020-12-06 11:21

from django.db import migrations, models
import django.db.models.deletion
import theNewStore.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(help_text='Enter new word', max_length=30, unique=True, verbose_name='word')),
                ('created_date', models.DateField(auto_now=True, verbose_name='createion date')),
                ('last_modified', models.DateField(auto_now_add=True, verbose_name='last modified')),
                ('word_type', models.CharField(choices=[(None, 'Word Type'), ('v', 'Verb'), ('n', 'Noun'), ('aj', 'Adjective'), ('av', 'Adverb')], default='-------', max_length=10, verbose_name='word type')),
                ('word_image', models.ImageField(blank=True, null=True, upload_to=theNewStore.models.image_file_path, verbose_name='an example image')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=theNewStore.models.audio_file_path, validators=[theNewStore.models.validate_audio_file], verbose_name='word Pronunciation')),
            ],
        ),
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_text', models.CharField(help_text="word's example", max_length=250, verbose_name='example')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theNewStore.wordmodel', verbose_name='word')),
            ],
        ),
        migrations.CreateModel(
            name='DefinitionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition_text', models.CharField(help_text="word's definition", max_length=250, verbose_name='definition')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theNewStore.wordmodel', verbose_name='word')),
            ],
        ),
    ]