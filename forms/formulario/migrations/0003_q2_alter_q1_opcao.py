# Generated by Django 5.0.1 on 2024-01-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_remove_q1_resposta_q1_opcao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Q2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(choices=[(1, 'A solução apresentada não atendeu as expectativas\u202f '), (2, 'A solução\u202fapresentada atendeu\u202fminimamente as expectativas'), (3, 'A solução apresentada atendeu parcialmente as expectativas\u202f '), (4, 'A solução apresentada atendeu plenamente as expectativas\u202f '), (5, 'A solução apresentada excedeu as expectativas\u202f ')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='q1',
            name='opcao',
            field=models.CharField(choices=[(1, 'Nenhum\u202fdos\u202f\u202frequisitos/necessidades\u202fforam\u202fidentificados\u202fe\u202fvalidados\u202fcom\u202fos\u202fusuários'), (2, 'Alguns\u202fdos\u202frequisitos/necessidades\u202fforam\u202fidentificados\u202fe\u202fvalidados\u202fcom\u202fos\u202fusuários\u202f(30\u202f%)'), (3, 'A\u202fmaior\u202fparte\u202fdos\u202frequisitos/necessidades\u202fforam\u202fidentificados\u202fe\u202fvalidados\u202fcom\u202fos\u202fusuários\u202f(70\u202f%)'), (4, 'Todos\u202fos\u202frequisitos/necessidades\u202fforam\u202fidentificados\u202fe\u202fvalidados\u202fcom\u202fos\u202fusuários'), (5, 'Foram\u202flevantados\u202f\u202fe\u202fvalidados\u202frequisitos/necessidades\u202falém\u202fdos\u202finicialmente\u202fsolicitados,\u202fagregando\u202fvalor\u202fao\u202fprojeto.')], max_length=1),
        ),
    ]