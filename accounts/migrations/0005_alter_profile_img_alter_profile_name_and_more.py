# Generated by Django 4.2 on 2023-05-07 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_profile_slug_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='profile_image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الإسم رابعى'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الكشف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='who_i',
            field=models.TextField(max_length=250, verbose_name='من انا'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='الإسم')),
                ('email', models.EmailField(max_length=50, verbose_name='الإيميل')),
                ('comments', models.TextField(max_length=250, verbose_name='التعليق')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-create_at',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_photos', models.ImageField(blank=True, null=True, upload_to='', verbose_name='صور العياده :')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='photo')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الإسم')),
                ('number', models.CharField(max_length=20, verbose_name='رقم الهاتف')),
                ('email', models.EmailField(max_length=50, verbose_name='الإيميل')),
                ('read', models.BooleanField(blank=True, null=True, verbose_name='تمت القراءة')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc', to='accounts.profile', verbose_name='doctor')),
            ],
        ),
    ]
