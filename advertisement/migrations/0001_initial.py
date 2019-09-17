# Generated by Django 2.2.4 on 2019-09-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, null=True)),
                ('video_link', models.URLField(max_length=2500)),
                ('budget', models.DecimalField(decimal_places=4, max_digits=14)),
                ('price_per_view', models.DecimalField(decimal_places=4, max_digits=7)),
                ('switch', models.BooleanField(default=False, null=True)),
            ],
            options={
                'db_table': 'advertisement',
            },
        ),
        migrations.CreateModel(
            name='AdvertisementCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ad_category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='advertisement.Advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.User')),
            ],
            options={
                'db_table': 'watch_history',
            },
        ),
        migrations.CreateModel(
            name='RewardHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.User')),
                ('watch_history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='advertisement.WatchHistory')),
            ],
            options={
                'db_table': 'reward_history',
            },
        ),
        migrations.CreateModel(
            name='AdvertisementTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.Advertisement')),
                ('interests_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.InterestsType')),
            ],
            options={
                'db_table': 'ad_target',
            },
        ),
        migrations.CreateModel(
            name='AdvertisementTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.Advertisement')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.Tag')),
            ],
            options={
                'db_table': 'ad_tag',
            },
        ),
        migrations.CreateModel(
            name='AdvertisementLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.Advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'ad_like',
            },
        ),
        migrations.AddField(
            model_name='advertisement',
            name='ad_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisement.AdvertisementCategory'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.Client'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='tag',
            field=models.ManyToManyField(through='advertisement.AdvertisementTag', to='advertisement.Tag'),
        ),
    ]
