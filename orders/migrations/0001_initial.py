# Generated by Django 4.0.6 on 2022-08-05 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('table', '0001_initial'),
        ('foodmenu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('order_note', models.CharField(blank=True, max_length=100)),
                ('order_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(choices=[('placed', 'placed'), ('delivered', 'delivered')], default='placed', max_length=50)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('add_ons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodmenu.addons')),
                ('menu_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodmenu.menuitem')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodmenu.size')),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table.table')),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
    ]