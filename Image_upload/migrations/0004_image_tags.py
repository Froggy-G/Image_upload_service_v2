# Generated by Django 3.2.5 on 2021-07-20 12:02

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('Image_upload', '0003_remove_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
