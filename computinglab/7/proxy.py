import asyncio, websockets

async def handle(websocket):
    msg = await websocket.recv()
    print(msg)

    uri="ws://localhost:8765"
    mess = input("enter msg:  ")

    async with websockets.connect(uri) as websocket:
        await websocket.send(mess)
        print("msg sent ")

async def main():
    async with websockets.serve(handle,"localhost",8766):
        print("listening")
        await asyncio.Future()


    



asyncio.run(main())


