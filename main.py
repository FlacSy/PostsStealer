import os 
import yaml
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
from telethon.tl.types import InputChannel
from telethon.tl.functions.channels import JoinChannelRequest

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

# Загружаем конфигурацию из файла
with open('config.yaml', 'r', encoding='utf-8') as config_file:
    config = yaml.safe_load(config_file)

source_channel_username = config['source_channel_username']
destination_channel_username = config['destination_channel_username']
send_media_content = config.get('send_media_content', True)
send_text = config.get('send_text', True)

client = TelegramClient('user_bot', api_id, api_hash)

async def main():
    await client.start(phone_number)
    print("Client connected")

    # Присоединяемся к каналам
    source_channel = await client.get_entity(source_channel_username)
    destination_channel = await client.get_entity(destination_channel_username)
    await client(JoinChannelRequest(channel=InputChannel(source_channel.id, source_channel.access_hash)))

    # Устанавливаем обработчик событий для новых сообщений
    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        # Проверяем конфигурацию для отправки сообщений с медиа контентом или без
        if send_media_content and event.media:
            if send_text:
                await client.send_message(destination_channel, event.message.text, file=event.media, link_preview=False)
            else:
                await client.send_file(destination_channel, file=event.media)
        elif send_text:
            await client.send_message(destination_channel, event.message.text)

    print("Listening for new messages...")

    # Бесконечный цикл для обработки событий
    while True:
        try:
            await client.run_until_disconnected()
        except Exception as e:
            print(f"An error occurred: {e}")
            # Переподключаемся при возможных ошибках
            await client.connect()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
