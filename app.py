import asyncio
import websockets
import time


async def echo_server(websocket):
    async for message in websocket:
        if message == 'received':
            continue
        print(f"Received message: {message}")
        response = ""
        if message == "Hello":
            response = "Hello from server"
        if message == "status":
            response = "new"
        if message == "new session":
            response = "ready"
        if message == "send":
            time.sleep(2)
            end_time = time.time() + 1
            while time.time() < end_time:
                response = "ready"
        if message == "stop":
            response = "stop"
        await asyncio.sleep(2)
        await websocket.send(response)

async def main():
    server = await websockets.serve(echo_server, "localhost", 8765)
    print("WebSocket server started")
    await server.wait_closed()

asyncio.run(main())
