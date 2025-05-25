
from django.http import JsonResponse, HttpResponse
import subprocess

def home(request):
    return HttpResponse('''
    <html><body style="text-align:center;margin-top:50px">
        <h1>🎮 WebCraft Launcher</h1>
        <button onclick="fetch('/launch/').then(r=>alert('Game launched'))"
        style="font-size:24px;padding:10px 40px;">▶ Play</button>
    </body></html>
    ''')

def launch_game(request):
    subprocess.Popen(['python', 'client_ursina.py'])
    return JsonResponse({'status': 'launched'})
