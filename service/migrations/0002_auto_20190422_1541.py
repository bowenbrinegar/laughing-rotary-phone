# Generated by Django 2.2 on 2019-04-22 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsteriodData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('x_pos', models.IntegerField()),
                ('y_pos', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AsteriodsBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HoopData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('x_pos', models.IntegerField()),
                ('y_pos', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HoopsBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PositionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('x_pos', models.IntegerField()),
                ('y_pos', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SpeedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('speed', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='livesLeft',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='timeLeft',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='FlightTracker',
        ),
        migrations.AddField(
            model_name='speeddata',
            name='flight_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Flight'),
        ),
        migrations.AddField(
            model_name='positiondata',
            name='flight_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Flight'),
        ),
        migrations.AddField(
            model_name='hoopsbundle',
            name='flight_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Flight'),
        ),
        migrations.AddField(
            model_name='hoopdata',
            name='hoop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.HoopsBundle'),
        ),
        migrations.AddField(
            model_name='asteriodsbundle',
            name='flight_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Flight'),
        ),
        migrations.AddField(
            model_name='asterioddata',
            name='asteriod_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.AsteriodsBundle'),
        ),
    ]
