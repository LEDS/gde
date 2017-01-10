# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='tipoAcumulo',
            field=models.ForeignKey(null=True, to='app.TipoAcumulo', blank=True, related_name='tipoAcumulo'),
        ),
    ]
