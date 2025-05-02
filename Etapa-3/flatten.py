def flatten(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten(item))  # Llamada recursiva si el item es una lista
        elif isinstance(item, tuple):
            flattened.extend(flatten(list(item)))  # Convertir la tupla en lista y aplanarla
        elif isinstance(item, dict):
            flattened.extend(flatten(list(item.items())))  # Convertir los diccionarios en lista de tuplas (key, value)
        else:
            flattened.append(item)  # Si no es lista, tupla ni diccionario, agregamos el item tal cual
    return flattened
