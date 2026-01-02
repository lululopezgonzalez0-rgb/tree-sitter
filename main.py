from highrise import BaseBot, User

class MiBotBienvenida(BaseBot):
    # Saludo automático cuando alguien entra a la sala
    async def on_user_join(self, user: User, position):
        await self.highrise.chat(f"¡Hola {user.username}! Bienvenido a la sala. Usa !ayuda para ver los comandos.")

    # Responder a comandos u órdenes por chat
    async def on_chat(self, user: User, message: str):
        if message.lower() == "!ayuda":
            await self.highrise.chat(f"Hola {user.username}, estas son mis órdenes disponibles: !reglas, !tienda.")
```

### 3. Ejecución del Bot
Una vez guardado tu archivo (ej. `main.py`), ejecútalo desde la terminal usando el siguiente comando:
`highrise main:MiBotBienvenida <RoomID> <Token>`.

### Recursos Adicionales
*   **Alojamiento 24/7:** Puedes usar servicios como [Replit](https://create.highrise.game/learn/bots/guides/cloud/replit) para mantener el bot activo permanentemente sin tener tu computadora encendida.
*   **Personalización:** Puedes cambiar la apariencia del bot (outfit) mediante la función `buy_item` o configurando su inventario en el portal.
