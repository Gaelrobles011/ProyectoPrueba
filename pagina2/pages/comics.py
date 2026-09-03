import reflex as rx
from pagina2.components.navbar import navbar
from pagina2.components.comics_navbar import comics_navbar
from pagina2.components.comics_grid import comics_grid
from pagina2.components.chat_bot import chat_bot

def comics() -> rx.Component:
    return rx.box(
        # Navbar Principal de Tienda_Gael
        navbar(),
        # Sub-Navbar con Buscador y Categorías
        comics_navbar(),
        # Contenido principal sobre el fondo de Cómic
        rx.vstack(
            rx.heading(
                "Ventas de Comics", 
                color="white", 
                size="8",
                bg="#1e5631",
                padding="15px 30px",
                border_radius="12px",
                border="2px solid #00ff66",
                margin_top="40px",
            ),
            # Grilla con las tarjetas y modal
            comics_grid(),
            spacing="5",
            align="center",
            min_height="80vh",
        ),
        chat_bot(),
        # Fondo temático de viñetas (con la diagonal inicial '/')
        background_image="url('/images/comic_bg.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        background_attachment="fixed",
        min_height="100vh",
    )