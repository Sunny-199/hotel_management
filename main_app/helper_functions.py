from .models import Menu, MenuCategory
from cryptography.fernet import Fernet


def get_or_create_menu(obj, hotel):
    menu, created = Menu.objects.get_or_create(name=obj.get("menu"), hotel=hotel)
    return menu


def get_or_create_menu_category(obj, menu):
    menu_category, created = MenuCategory.objects.get_or_create(name=obj.get("menu_category"), menu=menu)
    return menu_category


def encrypt_data(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(data.encode()).decode()
    # encMessage = fernet.encrypt(data.encode())
    return encMessage
    # print("original string: ", data)
    # print("encrypted string: ", encMessage)
    # decMessage = fernet.decrypt(encMessage).decode()


def get_role_id(data):
    if data.get('is_admin') and not data.get("is_general_manager"):
        role_id = 1
    elif data.get('is_general_manager') and not data.get('is_admin'):
        role_id = 2
    elif data.get('is_general_manager') and data.get('is_admin'):
        role_id = 2
    elif data.get('is_staff'):
        role_id = 3
    else:
        role_id = 4
    return role_id
