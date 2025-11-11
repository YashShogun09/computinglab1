import asyncio
import websockets

async def sendmsg():
    uri="ws://localhost:8765"
    

    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("enter msg:  ")
            await websocket.send(msg)
            print("msg sent ")

        


asyncio.run(sendmsg())