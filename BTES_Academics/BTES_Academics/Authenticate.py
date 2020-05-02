from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailBackend(object):
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if getattr(user, 'is_active') and success:
                return user
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
