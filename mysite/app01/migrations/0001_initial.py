# Generated by Django 3.0.3 on 2020-03-04 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('address', models.CharField(max_length=50, verbose_name='地址')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('state_province', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name': '出版商',
                'verbose_name_plural': '出版商',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('authors', models.ManyToManyField(to='app01.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.BooleanField(choices=[(0, '男'), (1, '女')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
    ]
