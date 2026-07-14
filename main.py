import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 1. ЗАПУСК ВСТРОЕННОГО САЙТА (ТВОЙ HTML КОД)
html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Крипто-Кошелек и 1win Ракетка</title>
    <script src="https://telegram.org"></script>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; background-color: #0e1621; color: #fff; margin: 0; padding: 15px; user-select: none; }
        .header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 15px; border-bottom: 1px solid #24303f; }
        .user-info { display: flex; align-items: center; gap: 10px; }
        .avatar { width: 40px; height: 40px; border-radius: 50%; background: #2481cc; display: flex; align-items: center; justify-content: center; font-weight: bold; overflow: hidden; }
        .balance-card { background: linear-gradient(135deg, #2481cc, #1a5a96); padding: 20px; border-radius: 12px; margin: 15px 0; text-align: center; }
        .balance-amount { font-size: 32px; font-weight: bold; margin-top: 5px; color: #fff; }
        .crash-container { background: #17212b; border-radius: 12px; padding: 15px; margin-top: 20px; text-align: center; border: 1px solid #24303f; }
        .game-screen { height: 160px; background: #0b1118; border-radius: 8px; position: relative; overflow: hidden; display: flex; justify-content: center; align-items: center; margin-bottom: 15px; }
        .multiplier { font-size: 46px; font-weight: bold; color: #4bc658; z-index: 10; }
        .rocket { position: absolute; bottom: 10px; left: 10px; font-size: 34px; transition: all 0.1s linear; }
        .input-box { width: 85%; padding: 10px; margin: 10px 0; border-radius: 6px; border: 1px solid #24303f; background: #0e1621; color: white; text-align: center; }
        .btn { background: #2481cc; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; width: 90%; font-size: 16px; }
        .btn.btn-claim { background: #4bc658; }
    </style>
</head>
<body>
    <div class="header">
        <div class="user-info"><div class="avatar" id="user-avatar">?</div><div id="username">Загрузка...</div></div>
        <div style="color: #2481cc; font-weight: bold; font-size: 14px;">Крипто Бот</div>
    </div>
    <div class="balance-card">
        <div style="opacity: 0.8; font-size: 14px;">Доступный баланс</div>
        <div class="balance-amount">100.00 USD</div>
    </div>
    <div class="crash-container">
        <h3 style="margin-top: 0; color: #2481cc; font-size: 18px; text-align: left;">🚀 1WIN CRASH (Ракетка)</h3>
        <div class="game-screen" id="screen">
            <div class="multiplier" id="mult-text">1.00x</div>
            <div class="rocket" id="rocket-obj">🚀</div>
        </div>
        <input type="number" id="bet-amount" class="input-box" value="10">
        <button class="btn" id="action-btn" onclick="startGame()">СТАРТ</button>
    </div>
    <script>
        const tg = window.Telegram.WebApp; tg.expand();
        const user = tg.initDataUnsafe?.user;
        if (user) { document.getElementById('username').innerText = user.username ? '@' + user.username : user.first_name; }
        let gameInterval, currentMultiplier = 1.00, crashPoint = 0, isRunning = false, betValue = 0;
        function startGame() {
            if (isRunning) return;
            betValue = parseFloat(document.getElementById('bet-amount').value);
            isRunning = true; currentMultiplier = 1.00; crashPoint = (Math.random() * 3.45 + 1.05).toFixed(2);
            const btn = document.getElementById('action-btn'); btn.className = "btn btn-claim"; btn.innerText = "ЗАБРАТЬ ВЫИГРЫШ"; btn.setAttribute("onclick", "claimWin()");
            gameInterval = setInterval(() => {
                currentMultiplier += 0.04; document.getElementById('mult-text').innerText = currentMultiplier.toFixed(2) + "x";
                if (currentMultiplier >= crashPoint) endGame(false);
            }, 100);
        }
        function claimWin() { if (isRunning) endGame(true); }
        function endGame(isWin) {
            clearInterval(gameInterval); isRunning = false;
            const btn = document.getElementById('action-btn'); btn.className = "btn"; btn.innerText = "СТАРТ"; btn.setAttribute("onclick", "startGame()");
            if (isWin) { document.getElementById('mult-text').innerText = "УСПЕЛ! " + currentMultiplier.toFixed(2) + "x"; }
            else { document.getElementById('mult-text').innerText = "💥 ВЗРЫВ!"; }
            tg.sendData(JSON.stringify({ action: "casino_result", bet: betValue, profit: isWin ? (betValue * currentMultiplier) : 0 }));
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Сервер сайта запущен на порту {port}")
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# 2. ЗАПУСК ЛОГИКИ ТЕЛЕГРАМ БОТА
TOKEN = "8908913545:AAFqVtBWMZNTrJQKGJxDPyi3wsSHC9iv77Y"
bot = telebot.TeleBot(TOKEN)

# ТВОЕ ОРИГИНАЛЬНОЕ ПРИВЕТСТВИЕ
text = "Приветствую тебя друг, ты попал в моего крипто бота ⌚, бот полностью верифицирован компанией @send, и не относится к ск@м схемам, все платежи покупки и продажи полностью безопасны в этом кругу. Удачного пользования"

@bot.message_handler(commands=['start'])
def start(msg):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Render автоматически подставит имя твоего сервиса сюда
    RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL", "https://my-tg-bot-ef0y.onrender.com")
    web_app_url = f"{RENDER_EXTERNAL_URL}/index.html"
    
    kb.add(KeyboardButton(text="Открыть кошелек 🚀", web_app=WebAppInfo(url=web_app_url)))
    bot.send_message(msg.chat.id, text, reply_markup=kb)

if __name__ == '__main__':
    print("Бот погнал слушать команды...")
    bot.infinity_polling()
