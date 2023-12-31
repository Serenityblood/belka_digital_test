# Generated by Django 3.2.20 on 2023-10-09 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0005_reportmodel_raws'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmodel',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='raws', to='auth.user', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
