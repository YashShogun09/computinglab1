import asyncio, websockets

async def handle(websocket):
    msg = await websocket.recv()
    print(msg)

async def main():
    async with websockets.serve(handle,"localhost",8765):
        print("listening")
        await asyncio.Future()


asyncio.run(main())