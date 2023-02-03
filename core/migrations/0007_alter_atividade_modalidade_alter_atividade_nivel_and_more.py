# Generated by Django 4.1.5 on 2023-02-03 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_atividade_data_fim_alter_atividade_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='modalidade',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='core.modalidade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='nivel',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='core.nivel'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='quantidade_limite',
            field=models.IntegerField(default='a', verbose_name='Quantidade e Limite'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='status',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='turma',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='core.turma'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='usuario',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.AlterField(
            model_name='espaco',
            name='nome',
            field=models.CharField(default='a', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='nome',
            field=models.CharField(default='a', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='nome',
            field=models.CharField(default='a', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='status',
            name='nome',
            field=models.CharField(default='a', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(default='a', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='turma',
            field=models.IntegerField(default='a', verbose_name='Ano'),
        ),
    ]