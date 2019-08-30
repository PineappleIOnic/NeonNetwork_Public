# Generated by Django 2.1.7 on 2019-03-11 08:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogposts',
            old_name='post',
            new_name='post_content',
        ),
        migrations.AddField(
            model_name='blogposts',
            name='dateposted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]