from telegram import InlineKeyboardButton
from categories import CATEGORY_NAMES

def create_main_menu_keyboard():
    """
    Creates the main menu keyboard with category buttons.
    
    Returns:
        A list of lists containing InlineKeyboardButton objects
    """
    keyboard = []
    
    # Create a button for each category
    for category_id, category_name in CATEGORY_NAMES.items():
        keyboard.append([InlineKeyboardButton(category_name, callback_data=category_id)])
    
    return keyboard
