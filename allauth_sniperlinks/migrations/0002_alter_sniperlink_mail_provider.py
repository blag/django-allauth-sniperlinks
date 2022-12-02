# Generated by Django 3.2.10 on 2022-12-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allauth_sniperlinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sniperlink',
            name='mail_provider',
            field=models.CharField(blank=True, choices=[('UNKNOWN', 'Unknown'), ('GMAIL', 'Gmail'), ('GSUITE', 'Gsuite'), ('YAHOO', 'Yahoo'), ('AOL', 'AOL'), ('ROGERS', 'ROGERS'), ('OUTLOOK', 'Outlook'), ('ICLOUD', 'iCloud'), ('CHARTER', 'Charter'), ('CENTURYLINK', 'CenturyLink'), ('ONEANDONE', '1and1'), ('COMCAST', 'Comcast'), ('COX', 'Cox'), ('SHAW', 'Shaw'), ('FASTMAIL', 'Fastmail'), ('FRONTIER', 'Frontier'), ('MAILDOTCOM', 'Mail_com'), ('EARTHLINK', 'Earthlink'), ('PRODIGY', 'Prodigy'), ('PROTONMAIL', 'ProtonMail'), ('JUNO', 'Juno'), ('NETADDRESS', 'NetAddress'), ('VIDEOTRON', 'Videotron'), ('WINDSTREAM', 'Windstream'), ('ZOHO', 'Zoho')], default='UNKNOWN', max_length=30, null=True),
        ),
    ]
