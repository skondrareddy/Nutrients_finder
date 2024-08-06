# Generated by Django 4.2.14 on 2024-08-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fruit_identifier", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fruitvegetable",
            name="nutrients",
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="calcium",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="calories",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="carbohydrates",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="fat",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="fiber",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="iron",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="magnesium",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="potassium",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="protein",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="sugar",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="vitamin_a",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="vitamin_b12",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="vitamin_b6",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="vitamin_c",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="fruitvegetable",
            name="vitamin_d",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="fruitvegetable",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
