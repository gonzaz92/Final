
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texto',
            field=models.TextField(default=1, max_length=3000),
            preserve_default=False,
        ),
    ]