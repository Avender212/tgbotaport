import telebot
from telebot import types
import logging
from categories import CATEGORY_NAMES, get_category_name, get_category_description

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Initialize the bot
TOKEN = "7882046046:AAF4zxPjELVTmWaIZZTvctVN-xCU6s0EfZk"
bot = telebot.TeleBot(TOKEN)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    """
    Handler for the /start command.
    Sends a welcome message with category selection buttons.
    """
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Create buttons for each category
    for category_id, category_name in CATEGORY_NAMES.items():
        button = types.InlineKeyboardButton(text=category_name, callback_data=category_id)
        markup.add(button)
    
    # Add Manager button
    manager_button = types.InlineKeyboardButton(text="👨‍💼 Менеджер", url="https://t.me/philagent")
    markup.add(manager_button)
    
    # Send welcome message with buttons
    bot.send_message(
        message.chat.id,
        "Вас приветствует официальный бот-каталог мебельного магазина \"Апорт-М\". 🏠\n\n"
        "Здесь вы можете ознакомиться с прайсом и товаром в наличии!\n\n"
        "Доставка во все города Казахстана, оплата любым удобным методом, есть рассрочка на 12 месяцев!\n\n"
        "По вопросу приобретения, а также по всем дополнительным вопросам наличия и т.д. - пишите менеджеру!\n\n"
        "Выберите категорию для просмотра товаров:",
        reply_markup=markup
    )

# Handler for callback queries (buttons)
@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    """
    Handler for callback queries from inline buttons.
    """
    if call.data == 'back_to_menu':
        # Return to main menu
        markup = types.InlineKeyboardMarkup(row_width=2)
        for category_id, category_name in CATEGORY_NAMES.items():
            button = types.InlineKeyboardButton(text=category_name, callback_data=category_id)
            markup.add(button)
        
        # Add Manager button
        manager_button = types.InlineKeyboardButton(text="👨‍💼 Менеджер", url="https://t.me/philagent")
        markup.add(manager_button)
        
        bot.edit_message_text(
            "Вас приветствует официальный бот-каталог мебельного магазина \"Апорт-М\". 🏠\n\n"
            "Здесь вы можете ознакомиться с прайсом и товаром в наличии!\n\n"
            "Доставка во все города Казахстана, оплата любым удобным методом, есть рассрочка на 12 месяцев!\n\n"
            "По вопросу приобретения, а также по всем дополнительным вопросам наличия и т.д. - пишите менеджеру!\n\n"
            "Выберите категорию для просмотра товаров:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
        return
    
    # Get category information
    category_id = call.data
    category_name = get_category_name(category_id)
    category_description = get_category_description(category_id)
    
    # Create "Back to menu" button
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="⬅️ Назад к категориям", callback_data="back_to_menu")
    markup.add(button)
    
    # Build response message
    message = (
        f"*{category_name}*\n\n"
        f"{category_description}\n\n"
        "В данной категории представлены следующие товары:\n"
        "- Скоро здесь появятся товары!\n\n"
        "Для получения подробной информации о наличии и ценах, "
        "свяжитесь с нашим менеджером @philagent"
    )
    
    # Send response
    bot.edit_message_text(
        message,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown'
    )

# Main entry point
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
