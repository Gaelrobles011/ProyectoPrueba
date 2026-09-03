import reflex as rx
from pagina2.components.carrusel import carousel
from pagina2.components.chat_bot import chat_bot
from pagina2.components.navbar import navbar
from pagina2.components.explora import seccion_explora
from pagina2.components.minicarrusel import mini_carrusel


def index() -> rx.Component:
    return rx.box(
        navbar(),  # Mantiene tu navbar flotando arriba
        
        # 1. El carrusel se queda completamente fijo y estático en el fondo
        rx.box(
            carousel(),
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100vh",
            z_index="1",
        ),
        
        # 2. Esta sección sube y tapa el carrusel de forma limpia
        rx.box(
            rx.vstack(
                rx.heading(
                    "Explora Nuestro Catalogo ",
                    size="8",
                    color="#00FF88",
                    margin_bottom="0.5em",
                ),
                rx.text(
                    "",
                    color="#A0AEC0",
                    size="4",
                    text_align="center",
                ),
                seccion_explora(),  # Tus 4 tarjetas interactivas
                mini_carrusel(), #carrusel añadido----
                align="center",
                max_width="1200px",
                margin="0 auto",
                spacing="4",
            ),
            id="descarga",
            width="100%",
            min_height="100vh",
            background="#050b08",  # Color sólido para tapar el carrusel
            position="relative",
            z_index="2",  # Pasa por encima del carrusel (z_index=1)
            margin_top="100vh",  # Empuja esta sección abajo para que el carrusel se vea primero
            padding_top="80px",
            padding_x="2em",
            border_top="2px solid rgba(0, 255, 136, 0.3)",
        ),
        chat_bot(),
        width="100%",
        position="relative",
    )