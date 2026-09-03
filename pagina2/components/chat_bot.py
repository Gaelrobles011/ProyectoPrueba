import reflex as rx
from google import genai

# Inicializa el cliente con tu API Key
client = genai.Client(api_key="AQ.Ab8RN6LZ-tWOXtJDVM3oel9tMWlun8Y5sve5lw67webh3IiXxw")

# Subimos el archivo de forma segura protegiéndolo por si ya existe
try:
    mi_catalogo_file = client.files.upload(file="catalogo_fantastic_world.pdf")
except Exception:
    # Si ya se subió antes o hay un detalle, lo buscamos de los archivos existentes
    mi_catalogo_file = client.files.get(name="files/catalogo_fantastic_world.pdf") # O usa la referencia directa

class ChatState(rx.State):
    messages: list[dict[str, str]] = [
        {
            "role": "model", 
            "content": "¡Hola! Soy el asistente virtual de tu tienda. ¿En qué te puedo ayudar hoy?"
        }
    ]
    current_message: str = ""

    def set_message(self, text: str):
        self.current_message = text

    def handle_submit(self):
        if not self.current_message.strip():
            return
        
        user_msg = self.current_message
        self.messages.append({"role": "user", "content": user_msg})
        self.current_message = ""
        
        self.messages.append({"role": "model", "content": "..."})

        try:
            # Llamada directa sin stream para evitar desconexiones de delta en Reflex
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[mi_catalogo_file, user_msg],
                config={
                    "system_instruction": "ERES EL ASISTENTE EXCLUSIVO DE 'Fantastic_World'. PROHIBIDO mencionar el nombre 'Geekverse Store' o cualquier otro nombre. Lee el documento adjunto y responde basándote única y exclusivamente en él.",
                },
            )
            
            # Asignamos la respuesta completa de golpe
            self.messages[-1]["content"] = response.text
                    
        except Exception as e:
            print(f"Error técnico: {e}")
            self.messages[-1]["content"] ="¡Vaya! Hemos alcanzado el límite temporal de consultas gratuitas de la IA por hoy. "
            "Inténtalo más tarde o revisa los detalles de tu plan."




            
BOT_AVATAR = "/images/camaleon.png"

def message_view(message: dict) -> rx.Component:
    is_user = message["role"] == "user"
    return rx.box(
        rx.text(
            message["content"], 
            color=rx.cond(is_user, "white", "black")
        ),
        background_color=rx.cond(is_user, "#2D6A4F", "#e2e8f0"),
        padding="10px",
        border_radius="10px",
        max_width="85%",
        align_self=rx.cond(is_user, "flex-end", "flex-start"),
    )

def chat_bot() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.box(
                rx.image(
                    src=BOT_AVATAR,
                    width="100%",
                    height="100%",
                    border_radius="50%",
                    object_fit="cover",
                ),
                position="fixed",
                bottom="20px",
                right="20px",
                width="65px",
                height="65px",
                border_radius="50%",
                background_color="white",
                padding="3px",
                cursor="pointer",
                z_index="1000",
                box_shadow="0 4px 12px rgba(0,0,0,0.25)",
            )
        ),
        rx.popover.content(
            rx.vstack(
                rx.hstack(
                    rx.image(src=BOT_AVATAR, width="35px", height="35px", border_radius="40%"),
                    rx.vstack(
                        rx.text("Asistente Virtual", weight="bold", color="white", size="2"),
                        rx.text("En línea", color="#a7f3d0", size="1"),
                        spacing="0",
                    ),
                    width="100%",
                    background_color="#2D6A4F",
                    padding="12px",
                    align="center",
                ),
                rx.box(
                    rx.vstack(
                        rx.foreach(ChatState.messages, message_view),
                        # Un elemento invisible al final para ayudar a anclar el scroll
                        rx.box(id="scroll-anchor"),
                        align_items="stretch",
                        spacing="3",
                        width="100%",
                    ),
                    height="280px",
                    width="100%",
                    padding="12px",
                    overflow_y="auto",
                    id="chat-container",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Escribe tu duda...",
                        value=ChatState.current_message,
                        on_change=ChatState.set_message,
                        width="100%",
                        size="2",
                        border_radius="20px",
                        color="black",
                    ),
                    rx.button(
                        "Enviar",
                        on_click=ChatState.handle_submit,
                        size="2",
                        background_color="#2D6A4F",
                        color="white",
                        border_radius="20px",
                        cursor="pointer",
                    ),
                    padding="10px",
                    width="100%",
                    border_top="1px solid #e2e8f0",
                ),
                width="320px",
                spacing="0",
            ),
            padding="0",
            border_radius="12px",
            box_shadow="0 10px 25px rgba(0,0,0,0.2)",
            background_color="white",
            overflow="hidden",
        ),
    )