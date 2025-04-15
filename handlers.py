from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from categories import CATEGORY_NAMES, get_category_name, get_category_description
from utils import create_main_menu_keyboard

def start(update: Update, context: CallbackContext):
    """
    Handler for the /start command.
    Sends a welcome message with category selection buttons.
    
    Args:
        update: The update object from Telegram
        context: The context object for the handler
    """
    keyboard = create_main_menu_keyboard()
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "Добро пожаловать в магазин мебели Апорт! 🏠\n\n"
        "У нас вы найдете качественную мебель для любого помещения в вашем доме.\n\n"
        "Выберите категорию для просмотра товаров:",
        reply_markup=reply_markup
    )

def button(update: Update, context: CallbackContext):
    """
    Handler for callback queries from inline buttons.
    
    Args:
        update: The update object from Telegram
        context: The context object for the handler
    """
    query = update.callback_query
    query.answer()
    
    category_id = query.data
    
    if category_id == 'back_to_menu':
        # Return to main menu
        keyboard = create_main_menu_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text="Выберите категорию для просмотра товаров:",
            reply_markup=reply_markup
        )
        return
    
    # Get category information
    category_name = get_category_name(category_id)
    category_description = get_category_description(category_id)
    
    # Create keyboard with products (would come from database in real implementation)
    # For now we'll just show a back button
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад к категориям", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Build response message
    message = (
        f"*{category_name}*\n\n"
        f"{category_description}\n\n"
        "В данной категории представлены следующие товары:\n"
        "- Скоро здесь появятся товары!\n\n"
        "Для получения подробной информации о наличии и ценах, "
        "свяжитесь с нашим консультантом по телефону +7 (XXX) XXX-XX-XX"
    )
    
    query.edit_message_text(
        text=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
