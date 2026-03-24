import csv

def read_csv(filepath):
    """Читает CSV файл и возвращает список словарей."""
    data = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"Успешно загружено {len(data)} строк из {filepath}")
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []
    

 # src/data_filter.py

def filter_by_value(data, field, value):
    """
    Фильтрует записи, где значение поля равно указанному.
    
    Args:
        data: список словарей
        field: название поля (ключ)
        value: значение для сравнения
    
    Returns:
        отфильтрованный список
    """
    result = []
    for row in data:
        if field in row and row[field] == value:
            result.append(row)
    return result

def filter_by_range(data, field, min_val, max_val):
    """
    Фильтрует записи, где значение поля в диапазоне [min_val, max_val].
    
    Args:
        data: список словарей
        field: название поля
        min_val: минимальное значение
        max_val: максимальное значение
    
    Returns:
        отфильтрованный список
    """
    result = []
    for row in data:
        if field in row:
            try:
                val = float(row[field])
                if min_val <= val <= max_val:
                    result.append(row)
            except (ValueError, TypeError):
                pass
    return result

def filter_by_text(data, field, text):
    """
    Поиск по тексту (частичное совпадение, регистронезависимо).
    
    Args:
        data: список словарей
        field: название поля
        text: искомый текст
    
    Returns:
        найденные записи
    """
    result = []
    text_lower = text.lower()
    
    for row in data:
        if field in row:
            row_value = str(row[field]).lower()
            if text_lower in row_value:
                result.append(row)
    return result

def sort_data(data, field, reverse=False):
    """
    Сортировка данных по полю.
    
    Args:
        data: список словарей
        field: поле для сортировки
        reverse: обратный порядок (True - по убыванию)
    
    Returns:
        отсортированный список
    """
    return sorted(data, key=lambda x: x.get(field, ''), reverse=reverse)   