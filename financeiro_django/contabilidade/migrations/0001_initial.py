# Generated by Django 4.2.10 on 2024-10-29 18:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome da cidade')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'cidade',
                'verbose_name_plural': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome da conta')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contabilidade.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
            },
        ),
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('data', models.DateField(verbose_name='Data de pagamento')),
                ('motivo', models.TextField(verbose_name='Motivo')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Valor')),
                ('anexo', models.FileField(blank=True, null=True, upload_to='anexo_mov/%Y/%m', verbose_name='Anexo')),
                ('status', models.CharField(max_length=15, verbose_name='Status')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('conta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contabilidade.conta', verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
