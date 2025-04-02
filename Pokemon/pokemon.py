class Pokemon:
    def __init__(self, nombre, defensa, ataque, tipo="N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.tipo = tipo

    def __str__(self):
        tipo_emojis = {
            "Fuego": "🔥",
            "Agua": "💧",
            "Hierba": "🌱",
            "Eléctrico": "⚡",
            "Roca": "🗻",
            "Hielo": "❄️",
            "Psíquico": "🔮",
            "Lucha": "🥊",
            "Venenoso": "☠️",
            "Volador": "🕊️",
            "Fantasma": "👻",
            "Fantasma / Psíquico": "👻 / 🔮",
            "Bicho": "🐛",
            "Dragón": "🐉",
            "N/A": "❓"
        }
        # Obtener el emoji correspondiente al tipo del Pokémon
        emoji = tipo_emojis.get(self.tipo, "❓")
        # Formatear la cadena de salida
        return f"{self.nombre} ({self.tipo}) {emoji}"
