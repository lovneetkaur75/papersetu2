# Generated by Django 5.2.3 on 2025-07-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0015_alter_userconferencerole_role_subreviewerinvite'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='confidence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
