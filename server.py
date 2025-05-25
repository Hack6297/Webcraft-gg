import os
import sys

# === ⬇️ Путь до каталога WebCraftLauncher/WebCraftLauncher/settings.py
sys.path.append(os.path.join(os.path.dirname(__file__), "WebCraftLauncher"))
sys.path.append(os.path.join(os.path.dirname(__file__), "WebCraftLauncher", "WebCraftLauncher"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django
django.setup()

from socketio import AsyncServer
from socketio.asgi import ASGIApp
from fastapi import FastAPI
import uvicorn

sio = AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
asgi_app = ASGIApp(sio)
app.mount("/", asgi_app)

players = {}

@sio.event
async def connect(sid, environ):
    print(f"[+] {sid} connected")
    players[sid] = {'x': 0, 'y': 0, 'z': 0, 'color': (255, 255, 255), 'nickname': 'Player'}
    await sio.emit('player_update', players)

@sio.event
async def disconnect(sid):
    print(f"[-] {sid} disconnected")
    players.pop(sid, None)
    await sio.emit('player_update', players)

@sio.event
async def player_position(sid, data):
    players[sid] = {
        'x': data['x'],
        'y': data['y'],
        'z': data['z'],
        'color': data['color'],
        'nickname': data.get('nickname', 'Player')
    }
    await sio.emit('player_update', players)

@sio.event
async def block_update(sid, data):
    await sio.emit('block_update', data, skip_sid=sid)

@sio.event
async def block_remove(sid, data):
    await sio.emit('block_remove', data, skip_sid=sid)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
