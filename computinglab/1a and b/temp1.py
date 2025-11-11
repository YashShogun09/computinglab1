import asyncio
import websockets

async def send_msg():
    msg = input("entr msg :  ")
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)

asyncio.run(send_msg())