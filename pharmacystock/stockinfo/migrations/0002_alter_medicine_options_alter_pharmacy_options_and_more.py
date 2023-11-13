# Generated by Django 4.2.7 on 2023-11-13 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'ordering': ['name'], 'verbose_name': 'Лекарство', 'verbose_name_plural': 'Лекарства'},
        ),
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'ordering': ['address'], 'verbose_name': 'Аптека', 'verbose_name_plural': 'Аптеки'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-quantity'], 'verbose_name': 'Запас', 'verbose_name_plural': 'Запасы'},
        ),
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='dosage',
            field=models.CharField(max_length=255, verbose_name='Дозировка'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='manufacturer',
            field=models.CharField(max_length=255, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название лекарства'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='prescription_required',
            field=models.CharField(max_length=255, verbose_name='Условия отпуска'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес аптеки'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='metro_station',
            field=models.CharField(max_length=255, verbose_name='Ближайшее метро'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='number',
            field=models.IntegerField(verbose_name='Номер аптеки'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockinfo.medicine', verbose_name='Лекарство'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockinfo.pharmacy', verbose_name='Аптека'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]