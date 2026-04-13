import logging

import redis.asyncio as redis

from settings.settings import settings


class RedisManager:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.redis = None

    async def connect(self):
        logging.info(f"Начинаю подключение к redis host={self.host}, port={self.port}")
        self.redis = await redis.Redis(host=self.host, port=self.port)
        logging.info(f"Успешное подключение к redis host={self.host}, port={self.port}")

    async def set(self, key: str, value: str, expire: int = None):
        if expire:
            await self.redis.set(key, value, ex=expire)
        else:
            await self.redis.set(key, value)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def disconnect(self):
        if self.redis:
            await self.redis.close()

redis_manager = RedisManager(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

#TODO: разобраться с этим местом - как это не хранить в main или только там можно?
# def redis_start():
#     await redis_manager.connect()
#     FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
#     logging.info("FastAPI cache initialized")
#     yield
#     await redis_manager.disconnect()