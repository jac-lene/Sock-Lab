# Generated by Django 4.0.6 on 2022-07-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socklab', '0005_alter_basicsock_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicsock',
            name='user_photo',
            field=models.TextField(blank=True, default='upload photo here'),
        ),
    ]
