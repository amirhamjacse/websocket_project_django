import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="Welcome to the WebSocket!")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=f"Echo: {text_data}")
        print("added print")
