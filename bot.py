import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "8681727417:AAH0p9f9X8B+Coding+TipX3A+2FcodeX0A0AFor+all+commands%2C+type+*2Fhelp*&reply_parameters=%77%2A4A5+welcome+to+the+4bdo+bot%21+Your+personal+smart+assistant.+%0A%0A%F0%9F%8E%AEABDO+V+ONLINE+%28GTA+5+Project%29%3A%0A%F0%9F%8E%ACMovies+%28Action+%26+Horror%29%3A%0A%F0%9F%8C%A3Fmovies%0A%0A%F0%9F%8E%8FFor+all+commands%3C%2C+type+%2A%2Fhelp%2A"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = (
        "🤖 Welcome to the Abdo Bot! Your personal & smart assistant.\n\n"
        "🎮 **ABDO V ONLINE (GTA 5 Project)**: /gta5\n"
        "🎬 **Movie Recommendations**: /movies\n"
        "💡 **Coding Tip**: /coding\n"
        "😂 **Developer Joke**: /joke\n"
        "📞 **Contact Developer**: /contact"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['gta5'])
def send_gta5(message):
    gta_text = (
        "🎮 ABDO V ONLINE (GTA 5 Project):\n\n"
        "• A legendary custom server combining action, open-world missions, and AI integration!\n"
        "• Built and managed by Abdo.\n"
        "• For inquiries and details, contact the developer directly on WhatsApp:\n"
        "https://wa.me/393717597434"
    )
    bot.reply_to(message, gta_text)

@bot.message_handler(commands=['movies'])
def send_movies_menu(message):
    menu_text = (
        "🎬 Choose a movie genre:\n\n"
        "🔥 Action Movies: Type /action\n"
        "😱 Horror Movies: Type /horror"
    )
    bot.reply_to(message, menu_text)

@bot.message_handler(commands=['action'])
def send_action_movies(message):
    action_text = (
        "🔥 Top 5 Action Movies:\n\n"
        "1. Mad Max: Fury Road - High-octane post-apocalyptic car chase.\n"
        "2. John Wick - Legendary assassin seeking vengeance.\n"
        "3. The Dark Knight - Batman faces the Joker in Gotham.\n"
        "4. Gladiator - Roman general seeks revenge in the arena.\n"
        "5. Inception - Mind-bending heist inside dreams."
    )
    bot.reply_to(message, action_text)

@bot.message_handler(commands=['horror'])
def send_horror_movies(message):
    horror_text = (
        "😱 Top 5 Horror Movies:\n\n"
        "1. The Conjuring - Paranormal investigators face dark spirits.\n"
        "2. Hereditary - A grieving family uncovers terrifying secrets.\n"
        "3. The Exorcist - Classic demonic possession story.\n"
        "4. A Nightmare on Elm Street - Freddy Krueger in dreams.\n"
        "5. It - Kids face a shape-shifting ancient evil."
    )
    bot.reply_to(message, horror_text)

@bot.message_handler(commands=['coding'])
def send_code_tip(message):
    bot.reply_to(message, "💡 Coding Tip: 'Bugs are just proof that your code is trying to build something completely new!'")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, "😂 Developer Joke: Why do programmers prefer dark mode? Because light attracts bugs!")

@bot.message_handler(commands=['contact'])
def send_contact(message):
    contact_text = (
        "📞 Contact Developer (Abdo):\n"
        "WhatsApp: +393717597434\n"
        "Direct Link: https://wa.me/393717597434"
    )
    bot.reply_to(message, contact_text)

@bot.message_handler(func=lambda m: True)
def all_messages(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Sorry, I am having trouble connecting right now. Try again later!")

print("Bot is running...")
bot.infinity_polling()
