#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCraftLauncher.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcraft_launcher_site.settings')
>>>>>>> 2c7ea8b6258db0972324c1d5aa873a98296caee6
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)
