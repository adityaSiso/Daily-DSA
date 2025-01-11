import websockets
import asyncio
import time

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        msg = input('Who?')
        await websocket.send(msg)
        print(f'Client Sent: {msg}')

        resp = await websocket.recv()
        print(f'Client Received: {resp}')


asyncio.run(client())