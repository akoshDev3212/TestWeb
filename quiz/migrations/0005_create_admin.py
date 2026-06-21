from django.db import migrations
from django.contrib.auth import get_user_model

def create_admins(apps, schema_editor):
    User = get_user_model()
    # Akosh3212 adminini yaratish
    if not User.objects.filter(username='Akosh3212').exists():
        User.objects.create_superuser('Akosh3212', 'akosh@example.com', 'Akosh3212')
    
    # Bunyodd1 adminini yaratish
    if not User.objects.filter(username='Bunyodd1').exists():
        User.objects.create_superuser('Bunyodd1', 'bunyod@example.com', 'Bunyodd1')

class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0004_question_difficulty_alter_question_correct_answer_and_more'), # O'zingizning oxirgi migratsiyangiz nomi
    ]

    operations = [
        migrations.RunPython(create_admins),
    ]