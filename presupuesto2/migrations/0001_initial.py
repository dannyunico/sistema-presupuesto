# Generated by Django 4.1.5 on 2023-02-13 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=500)),
                ('Numero_Factura', models.CharField(max_length=500)),
                ('Cod_Factura', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=500)),
                ('titulo', models.CharField(max_length=500)),
                ('COP', models.DecimalField(decimal_places=2, max_digits=15)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='LaborIndirecta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=500)),
                ('nombre', models.CharField(max_length=500)),
                ('jornal', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('unidad', models.CharField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cantidad', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='presupuesto2.factura')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='Herramientas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='herramientas', to='presupuesto2.herramientas'),
        ),
        migrations.AddField(
            model_name='factura',
            name='LaborIndirecta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laborindirecta', to='presupuesto2.laborindirecta'),
        ),
        migrations.AddField(
            model_name='factura',
            name='Material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='presupuesto2.material'),
        ),
    ]
