def load_respuestas():
    links = ["comienzo", "arturito", "departamentos", "calendario", "deportes"]
    respuestas = {}

    for link in links:
        path = f"'respuestas/{link}.txt'"
        key = link
        with open(path, 'r', encoding="utf-8") as file:
            respuestas[key] = file.read()

    return respuestas
