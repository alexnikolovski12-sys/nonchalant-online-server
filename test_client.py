import asyncio
import websockets

SERVER_URL = "wss://nonchalant-online-server.onrender.com/ws"

async def main():
    async with websockets.connect(SERVER_URL) as ws:
        print("Connected to server!")

        await ws.send("hello from client")
        while True:
            msg = await ws.recv()
            print("Received:", msg)

asyncio.run(main())
