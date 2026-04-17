print("СИСТЕМА СТАТУСОВ ЗАКАЗОВ")

status = input("Введите код статуса вашего заказа (pending, processing, shipped, delivered, cancelled): ")

match status:
    case "pending":
        state = "В ожидании 🕐"
        description = "Ваш заказ находится в зоне ожидания обработки"
        time = "1-2 дня"
        recommendation = "Ожидайте уведомления об обработке"
    case "processing":
        state = "В обработке 🕐"
        description = "Ваш заказ обрабатывается"
        time = "2 дня"
        recommendation = "Ожидайте уведомления об отправлении"
    case "shipped":
        state = "Отправлено ✈️"
        description = "Ваш заказ находится в пути"
        time = "3-5 дней"
        recommendation = "Следите за уведомлениями о доставке"
    case "delivered":
        state = "Доставлено 📦"
        description = "Ваш заказ доставлен на пункт выдачи"
        time = "0 дней"
        recommendation = "Заберите ваш заказ на пункте выдачи"
    case "cancelled":
        state = "Отменено ❌"
        description = "Ваш заказ был отменён"
        time = "0 дней"
        recommendation = "Сожалеем что вам пришлось отменить заказ("
    case _:
        print("Ошибка: неизвестный статус 'invalid_status'")
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")
        exit()

print("=" * 43)
print("=", " " * 5, "📦 СТАТУС ВАШЕГО ЗАКАЗА 📦", " " * 5, "=")
print("=" * 43)
print(f"Статус: {state}")
print(f"Описание: {description}")
print(f"Примерное время: {time}")
print(f"Рекомендация: {recommendation}")