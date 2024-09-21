# Анонимный чат-бот по интересам для Telegram

Это анонимный чат-бот для Telegram, который соединяет пользователей на основе их интересов. Пользователи могут выбрать интерес из списка, и бот найдет им собеседника с таким же интересом для приватного общения. В любой момент можно завершить диалог и выбрать другой интерес.

## Возможности
- Выбор интересов из списка.
- Автоматическое соединение с собеседником на основе выбранного интереса.
- Простое общение с использованием inline-кнопок.
- Возможность завершить чат и выбрать новый интерес.

## Как это работает
1. Пользователь запускает бота командой `/start`.
2. Бот предлагает список интересов с помощью inline-кнопок.
3. Пользователь выбирает интерес, и бот ищет другого пользователя с таким же интересом.
4. Как только найден собеседник, начинается анонимное общение.
5. Пользователь может завершить диалог и выбрать новый интерес в любой момент.

## Установка и запуск

### Требования
- Python 3.8+
- Библиотека `aiogram`

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/anonymous-chatbot.git
   cd anonymous-chatbot
   ```

2. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Укажите свой токен API Telegram в переменной `API_TOKEN` в коде:
   ```python
   API_TOKEN = 'ВАШ_API_ТОКЕН_БОТА'
   ```

4. Запустите бота:
   ```bash
   python bot.py
   ```

### Команды бота

- `/start`: Показывает приветственное сообщение с выбором интересов через inline-кнопки.

### Как пользоваться
1. **Запустите бота**, введя команду `/start`.
2. **Выберите интерес** из предложенного списка с помощью inline-кнопок.
3. **Ожидайте**, пока бот найдет собеседника с таким же интересом.
4. **Начните общение** с анонимным собеседником.
5. Чтобы **завершить диалог**, нажмите кнопку "Завершить диалог", которая вернет вас к выбору интересов.

### Проблемы и улучшения

#### Известные проблемы
- После выбора интереса, повторный выбор другого интереса пока не работает.
- После нахождения собеседника необходимо вернуться к исходному сообщению и выбрать "Завершить диалог", чтобы выйти из беседы.
- Reply-кнопки не работают как ожидалось, отправляя обычный текст, а не выполняя действия бота.

#### Возможные улучшения
- После создания чата должна оставаться только кнопка "Завершить диалог", чтобы позволить пользователю завершить беседу и вернуться к выбору интересов.
- Улучшить логику повторного выбора интересов, чтобы пользователи могли изменять интересы, не завершив беседу.
