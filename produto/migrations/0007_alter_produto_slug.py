# Generated by Django 4.0.3 on 2022-03-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produto_preco_alter_produto_preco_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
