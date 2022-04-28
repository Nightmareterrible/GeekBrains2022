def nightmareterrible_bio(name="empty", email="empty", date_birth="empty", phone="empty", city="empty"):
    """Выводит данные пользователя в виде словаря (одной строкой)"""
    bio = {"name": name, "email": email, "date_birth": date_birth, "phone": phone, "city": city}
    print(f"Данные пользователя: {bio}")


nightmareterrible_bio("Вася", "vasya123@roboclever.by", "01/01/2010", "+375123456789", "Пинск")
