import asyncio
import websockets

async def sendmsg():
    uri="ws://localhost:8765"
    msg = int(input("enter msg:  "))

    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
        print("msg sent ")


asyncio.run(sendmsg())

