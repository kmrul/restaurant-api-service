# Generated by Django 4.0.1 on 2022-01-20 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_candidate_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.candidate'),
        ),
    ]