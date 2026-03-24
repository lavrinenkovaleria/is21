# src/stats_calculator.py

def calculate_stats(data, field):
    """
    Вычисляет основные статистики для числового поля.
    
    Args:
        data: список словарей
        field: название поля
    
    Returns:
        словарь со статистиками
    """
    # Собираем все числовые значения
    values = []
    for row in data:
        if field in row:
            try:
                # Пробуем преобразовать в число
                val = float(row[field])
                values.append(val)
            except (ValueError, TypeError):
                # Если не число - пропускаем
                pass
    
    if not values:
        return {
            'count': 0,
            'min': None,
            'max': None,
            'sum': 0,
            'average': 0
        }
    
    # Сортируем для медианы
    values.sort()
    n = len(values)
    
    # Простые статистики
    count = n
    min_val = values[0]
    max_val = values[-1]
    sum_val = sum(values)
    avg_val = sum_val / n
    
    # Медиана (середина)
    if n % 2 == 0:
        median = (values[n//2 - 1] + values[n//2]) / 2
    else:
        median = values[n//2]
    
    return {
        'count': count,
        'min': round(min_val, 2),
        'max': round(max_val, 2),
        'sum': round(sum_val, 2),
        'average': round(avg_val, 2),
        'median': round(median, 2)
    }


def count_by_value(data, field):
    """
    Подсчитывает, сколько раз встречается каждое значение.
    
    Args:
        data: список словарей
        field: название поля
    
    Returns:
        словарь {значение: количество}
    """
    counts = {}
    
    for row in data:
        if field in row:
            value = row[field]
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
    
    return counts


def get_max_min(data, field):
    """
    Находит максимальное и минимальное значение в поле.
    
    Args:
        data: список словарей
        field: название поля
    
    Returns:
        кортеж (min, max)
    """
    values = []
    for row in data:
        if field in row:
            try:
                values.append(float(row[field]))
            except (ValueError, TypeError):
                pass
    
    if not values:
        return (None, None)
    
    return (min(values), max(values))


def group_count(data, group_field):
    """
    Группирует записи по значению поля и считает количество.
    
    Args:
        data: список словарей
        group_field: поле для группировки
    
    Returns:
        словарь {группа: количество}
    """
    groups = {}
    
    for row in data:
        key = row.get(group_field, 'Unknown')
        groups[key] = groups.get(key, 0) + 1
    
    return groups