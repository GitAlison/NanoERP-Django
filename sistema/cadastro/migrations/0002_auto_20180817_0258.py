# Generated by Django 2.2 on 2018-08-17 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='cpg',
            new_name='cpf_cnpj',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='rg',
            new_name='rg_ie',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='doc_tipo',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
