# Define furniture categories with emoji icons and display names

# Dictionary mapping category IDs to their display names
CATEGORY_NAMES = {
    'sofas': '🛋️ Диваны',
    'living_rooms': '🏠 Гостиные',
    'hallways': '🚪 Прихожие',
    'kitchen': '🍽️ Кухня',
    'bedroom': '🛌 Спальня',
    'children_rooms': '👶 Детская',
    'office': '💼 Офис'
}

# Dictionary with category descriptions
CATEGORY_DESCRIPTIONS = {
    'sofas': 'Комфортные диваны различных форм и размеров. От классических до современных моделей. Прямые, угловые, раскладные и модульные системы.',
    'living_rooms': 'Современные гостиные для вашего комфортного отдыха. Стенки, шкафы, тумбы под ТВ и журнальные столики в различных стилях и ценовых категориях.',
    'hallways': 'Функциональные прихожие, которые помогут организовать пространство и создать приятное первое впечатление о вашем доме. Шкафы, обувницы и вешалки.',
    'kitchen': 'Кухонные гарнитуры, обеденные столы и стулья для создания уютной и практичной кухни. Модульные системы и готовые решения.',
    'bedroom': 'Спальные гарнитуры, кровати, матрасы, шкафы и прикроватные тумбы для комфортного отдыха и здорового сна.',
    'children_rooms': 'Безопасная и удобная мебель для детей всех возрастов, от малышей до подростков. Кроватки, столы, шкафы и игровая мебель.',
    'office': 'Рабочие столы, компьютерные кресла, шкафы и стеллажи для организации эффективного рабочего пространства дома или в офисе.'
}

def get_category_name(category_id):
    """
    Get the display name for a given category ID.
    
    Args:
        category_id: The ID of the category
    
    Returns:
        The display name of the category, or the category ID if not found
    """
    return CATEGORY_NAMES.get(category_id, category_id)

def get_category_description(category_id):
    """
    Get the description for a given category ID.
    
    Args:
        category_id: The ID of the category
    
    Returns:
        The description of the category, or a default message if not found
    """
    return CATEGORY_DESCRIPTIONS.get(
        category_id, 
        "Информация о данной категории скоро появится. Пожалуйста, обратитесь к консультанту для получения дополнительной информации."
    )
