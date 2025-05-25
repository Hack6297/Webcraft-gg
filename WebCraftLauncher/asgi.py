import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCraftLauncher.settings')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCraftLauncher.settings')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebCraft.settings")


application = get_asgi_application()
