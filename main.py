from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

API_TOKEN = '8908913545:AAFqVtBWMZNTrJQKGJxDPyi3wsSHC9iv77Y'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Текст приветствия, который вы просили добавить
    welcome_text = (
        "Здравствуй мой друг, ты попал в крипто бота основного на компании @send, "
        "данная компания полностью дала разрешение и подтвердила что данный бот "
        "не нарушает правил платформы телеграмма, а также не занимается мошенической схемой."
    )
    
    # Кнопка для открытия Web App с вашей ссылкой на Render
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="🚀 Запустить приложение", 
            web_app=WebAppInfo(url="https://my-tg-bot-ef0y.onrender.com")
        )
    )
    
    await message.reply(welcome_text, reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Wallet App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="dark-theme">

    <!-- Шапка приложения -->
    <header class="header">
        <div class="user-info">
            <div class="avatar">?</div>
            <span class="status">Загрузка...</span>
        </div>
        <button class="settings-btn" onclick="toggleSettings()">⚙️</button>
    </header>

    <!-- Основной контейнер кошелька (Стиль Tonkeeper) -->
    <main class="wallet-container">
        <div class="balance-card">
            <p class="balance-label">Доступный баланс</p>
            <!-- Бесконечный баланс, как заказывали -->
            <h1 class="balance-amount">∞ USD</h1> 
        </div>

        <!-- Кнопки действий прямо под балансом -->
        <div class="action-buttons">
            <button class="action-btn"><span>➕</span>Пополнить</button>
            <button class="action-btn"><span>📤</span>Вывести</button>
            <button class="action-btn" onclick="openP2P()"><span>🤝</span>P2P Маркет</button>
        </div>

        <!-- Курс валют -->
        <div class="crypto-rates">
            <div class="rate-item">
                <span class="coin">💎 TON</span>
                <span class="price">$5.42</span>
            </div>
            <div class="rate-item">
                <span class="coin">🪙 BTC</span>
                <span class="price">$64,250</span>
            </div>
        </div>

        <!-- Блок игры 1WIN CRASH (Ракетка) -->
        <section class="crash-game">
            <h2 class="game-title">🚀 1WIN CRASH (Ракетка)</h2>
            <div class="game-screen">
                <div class="multiplier" id="multiplier">1.00x</div>
                <div class="rocket" id="rocket">🚀</div>
            </div>
            <div class="bet-controls">
                <input type="number" class="bet-input" value="10" min="1">
                <button class="start-btn" onclick="startRocket()">СТАРТ</button>
            </div>
        </section>
    </main>

    <!-- Модальное окно настроек -->
    <div class="modal" id="settingsModal">
        <div class="modal-content">
            <h3>Настройки</h3>
            <div class="setting-row">
                <label>Язык:</label>
                <select><option>Русский</option><option>English</option></select>
            </div>
            <div class="setting-row">
                <label>Валюта:</label>
                <select><option>USD</option><option>RUB</option><option>EUR</option></select>
            </div>
            <div class="setting-row">
                <label>Тема:</label>
                <select id="themeSelect" onchange="changeTheme()">
                    <option value="dark">Темная</option>
                    <option value="light">Светлая</option>
                </select>
            </div>
            <div class="setting-row">
                <label>Номер телефона:</label>
                <input type="tel" placeholder="+7 (999) 000-00-00">
            </div>
            <button class="close-btn" onclick="toggleSettings()">Закрыть</button>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>

:root {
    --bg-color: #0b141c;
    --card-bg: #16222f;
    --accent-blue: #2481cc;
    --text-main: #ffffff;
    --text-muted: #7e8b98;
    --green: #2ecc71;
}

.light-theme {
    --bg-color: #f0f4f8;
    --card-bg: #ffffff;
    --accent-blue: #1a73e8;
    --text-main: #1c1c1c;
    --text-muted: #5f6368;
}

body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Шапка */
.header {
    width: 100%;
    max-width: 450px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
    box-sizing: border-box;
}

.user-info { display: flex; align-items: center; gap: 10px; }
.avatar { background: var(--accent-blue); width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.settings-btn { background: none; border: none; font-size: 20px; cursor: pointer; }

/* Кошелек */
.wallet-container {
    width: 100%;
    max-width: 450px;
    padding: 10px 15px;
    box-sizing: border-box;
}

.balance-card {
    background: linear-gradient(135deg, #1d3557, var(--accent-blue));
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin-bottom: 15px;
}
.balance-label { color: rgba(255,255,255,0.7); font-size: 14px; margin: 0; }
.balance-amount { font-size: 32px; margin: 5px 0 0 0; }

/* Кнопки действий */
.action-buttons {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 20px;
}
.action-btn {
    flex: 1;
    background: var(--card-bg);
    border: none;
    color: var(--text-main);
    padding: 12px;
    border-radius: 12px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    font-size: 13px;
    font-weight: bold;
}

/* Курсы */
.crypto-rates {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 20px;
}
.rate-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.rate-item:last-child { border: none; }

/* Игра Ракетка */
.crash-game {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 15px;
}
.game-title { font-size: 16px; color: var(--accent-blue); margin-top: 0; }
.game-screen {
    background: #090f16;
    height: 180px;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}
.multiplier { font-size: 42px; color: var(--green); font-weight: bold; z-index: 2; }
.rocket {
    font-size: 35px;
    position: absolute;
    bottom: 10px;
    left: 10px;
    transition: transform 0.1s linear;
}

/* Элементы управления ставкой */
.bet-controls { display: flex; flex-direction: column; gap: 10px; margin-top: 15px; }
.bet-input {
    background: #090f16;
    border: 1px solid #233549;
    color: white;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
    font-size: 16px;
}
.start-btn {
    background: var(--accent-blue);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    font-size: 16px;
}

/* Настройки (Модальное окно) */
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6);
    justify-content: center;
    align-items: center;
    z-index: 10;
}
.modal-content {
    background: var(--card-bg);
    padding: 20px;
    border-radius: 16px;
    width: 85%;
    max-width: 350px;
}
.setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}
.setting-row select, .setting-row input {
    background: #090f16;
    border: 1px solid #233549;
    color: white;
    padding: 6px;
    border-radius: 6px;
}
.close-btn { width: 100%; padding: 10px; background: #e74c3c; color: white; border: none; border-radius: 8px; cursor: pointer; }
// Переключение окна настроек
function toggleSettings() {
    const modal = document.getElementById('settingsModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex';
}

// Смена темы (Светлая / Темная)
function changeTheme() {
    const theme = document.getElementById('themeSelect').value;
    if (theme === 'light') {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }
}

// Заглушка для P2P-маркета
function openP2P() {
    alert("Открытие P2P Маркета: здесь пользователи смогут размещать свои объявления об обмене.");
}

// Логика полета ракетки
let gameInterval;
function startRocket() {
    // Сброс позиций перед стартом
    clearInterval(gameInterval);
    const rocket = document.getElementById('rocket');
    const multiplierText = document.getElementById('multiplier');
    
    let currentMultiplier = 1.00;
    let posX = 10;
    let posY = 10;

    rocket.style.transform = `translate(0px, 0px) rotate(0deg)`;

    // Случайный момент взрыва ракетки (от 1.1 до 5.0x)
    const crashPoint = (Math.random() * 4 + 1.1).toFixed(2);

    gameInterval = setInterval(() => {
        currentMultiplier += 0.02;
        multiplierText.innerText = currentMultiplier.toFixed(2) + 'x';

        // Движение ракетки по диагонали вверх
        if (posX < 220) posX += 1.5;
        if (posY < 100) posY += 1.0;
        
        rocket.style.bottom = `${10 + posY}px`;
        rocket.style.left = `${10 + posX}px`;
        rocket.style.transform = `rotate(-15deg)`; // Наклон при полете

        // Проверка на краш (взрыв)
        if (currentMultiplier >= crashPoint) {
            clearInterval(gameInterval);
            multiplierText.style.color = '#e74c3c';
            multiplierText.innerText = `ВЗРЫВ: ${currentMultiplier.toFixed(2)}x`;
            rocket.style.transform = `scale(0) rotate(0deg)`; // Исчезновение
            
            // Возврат в исходное состояние через 2 секунды
            setTimeout(() => {
                multiplierText.style.color = '#2ecc71';
                multiplierText.innerText = '1.00x';
                rocket.style.bottom = '10px';
                rocket.style.left = '10px';
                rocket.style.transform = `scale(1) rotate(0deg)`;
            }, 2000);
        }
    }, 50);
}
