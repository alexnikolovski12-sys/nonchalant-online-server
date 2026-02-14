import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

connected_clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connected_clients.append(ws)
    print("Client connected")

    try:
        while True:
            data = await ws.receive_text()

            # Broadcast to all other clients
            for client in connected_clients:
                if client != ws:
                    await client.send_text(data)

    except WebSocketDisconnect:
        print("Client disconnected")
        connected_clients.remove(ws)

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
