# Generated by Django 4.2.1 on 2023-05-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_text_comment_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='password',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
