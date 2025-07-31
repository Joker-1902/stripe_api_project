from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        import stripe
        from django.conf import settings
        if hasattr(settings, 'STRIPE_SECRET_KEY'):
            stripe.api_key = settings.STRIPE_SECRET_KEY
