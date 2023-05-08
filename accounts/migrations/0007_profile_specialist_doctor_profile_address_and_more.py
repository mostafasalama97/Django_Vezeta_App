# Generated by Django 4.2 on 2023-05-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_waiting_time_profile_facebook_profile_google_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Specialist_doctor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='متخصص فى ؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='المحافظه'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='العنوان بالتفصيل'),
        ),
        migrations.AddField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('مخ وأعصاب', 'مخ وأعصاب'), ('جراحة أورام', 'جراحة أورام'), ('جلدية', 'جلدية'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('قلب وأوعيه دموية', 'قلب وأوعيه دموية'), ('أمراض دم', 'أمراض دم'), ('باطنة', 'باطنة'), ('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'), ('جراحة تجميل', 'جراحة تجميل'), ('أسنان', 'أسنان'), ('أطفال حديثي الولادة', 'أطفال حديثي الولادة'), ('نساء وتوليد', 'نساء وتوليد'), ('عظام', 'عظام'), ('جراحة أطفال', 'جراحة أطفال'), ('جراحة سمنة ومناظير ', 'جراحة سمنة ومناظير '), ('أورام', 'أورام'), ('جراحة أوعيه دموية', 'جراحة أوعيه دموية'), ('نفسي', 'نفسي')], max_length=50, null=True, verbose_name='دكتور ؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='join_us',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت الانضمام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_doctors',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=20, null=True, verbose_name='النوع'),
        ),
    ]
