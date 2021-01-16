# Generated by Django 2.2.3 on 2019-09-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190901_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Patient'), (2, 'Doctor'), (3, 'Deliveryman')], primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='accounts.Role'),
        ),
    ]