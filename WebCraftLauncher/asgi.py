import os
from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCraftLauncher.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebCraft.settings")
>>>>>>> 2c7ea8b6258db0972324c1d5aa873a98296caee6

application = get_asgi_application()
