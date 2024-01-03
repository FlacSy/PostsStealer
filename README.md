# PostStealer

**PostStealer** - это скрипт на Python, использующий библиотеку Telethon для автоматического пересылания сообщений из одного телеграм-канала в другой. Скрипт предоставляет гибкие настройки для отправки как текстовых сообщений, так и медиа-контента.

## Требования
- Python 3.6 и выше
- Учетная запись Telegram с полученными API-ключами (API_ID, API_HASH)
- Установленные зависимости, указанные в файле requirements.txt
  ```bash
  pip install -r requirements.txt
  ```

## Установка и настройка

1. **Клонирование репозитория**
    ```bash
    git clone https://github.com/your_username/PostStealer.git
    cd PostStealer
    ```

2. **Установка зависимостей**
    ```bash
    pip install -r requirements.txt
    ```

3. **Настройка переменных окружения**
    Создайте файл `.env` и укажите в нем свои значения для `API_ID`, `API_HASH` и `PHONE_NUMBER`.
    ```
    API_ID=your_api_id
    API_HASH=your_api_hash
    PHONE_NUMBER=your_phone_number
    ```

4. **Настройка конфигурации**
    Отредактируйте файл `config.yaml` согласно вашим предпочтениям.
    ```yaml
    source_channel_username: '@source_channel_username'
    destination_channel_username: '@destination_channel_username'
    send_media_content: true
    send_text: true
    ```

## Запуск

```bash
python your_script_name.py
```

## Описание конфигурации

- **source_channel_username**: Имя пользователя (Username) исходного канала, откуда будут пересылаться сообщения.
- **destination_channel_username**: Имя пользователя (Username) целевого канала, куда будут отправляться сообщения.
- **send_media_content**: Определяет, должен ли скрипт отправлять медиа-контент (изображения, видео и т. д.).
- **send_text**: Определяет, должен ли скрипт отправлять текстовые сообщения.

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).

**Примечание:** Использование данного скрипта может быть ограничено правилами и политикой Telegram API. Пожалуйста, убедитесь, что соблюдаете все правила Telegram при использовании этого скрипта.