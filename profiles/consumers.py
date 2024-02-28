import json
import random
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class SentenceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket Connected...")
        self.connected = True
        await self.send_sentence()

    async def disconnect(self, close_code):
        self.connected = False
        print("WebSocket Disconnected...")

    async def send_sentence(self):
        while self.connected:
            sentence = f"This is a random sentence: {random.randint(1, 100)}"
            print(sentence)
            await self.send(text_data=json.dumps({"sentence": sentence}))
            await asyncio.sleep(5)

    async def receive(self, text_data):
        pass
