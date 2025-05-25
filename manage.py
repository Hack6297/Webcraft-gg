#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcraft_launcher_site.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebCraftLauncher.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcraft_launcher_site.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)
