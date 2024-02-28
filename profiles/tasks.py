from celery import shared_task
import os
from .models import UserProfile
from django.core.files.base import ContentFile
from django.core.files import File

@shared_task
def process_profile_picture(file_path, user_id):
    try:
        with open(file_path, 'rb') as file:
            user_profile = UserProfile.objects.get(id=user_id)
            user_profile.profile_picture.save(os.path.basename(file_path), File(file))

        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        return {'status': 'success', 'word_count': word_count}
    except FileNotFoundError:
        return {'status': 'error', 'message': 'File not found'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

