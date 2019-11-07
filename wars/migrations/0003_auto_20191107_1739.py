# Generated by Django 2.2.7 on 2019-11-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0002_auto_20191107_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='war',
            name='major_players',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('major_players', models.CharField(max_length=1000)),
                ('key_technologies', models.CharField(max_length=500)),
                ('winner', models.CharField(max_length=500)),
                ('war', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battles', to='wars.War')),
            ],
        ),
    ]
