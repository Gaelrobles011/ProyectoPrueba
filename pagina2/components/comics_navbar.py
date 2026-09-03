import reflex as rx
from pagina2.state.comics_state import ComicsState

def comics_navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Contenedor izquierdo: Botón de inicio + Buscador
            rx.hstack(
                rx.link(
                    rx.button(
                        "🚪",
                        variant="ghost",
                        size="3",
                        cursor="pointer",
                        _hover={"transform": "scale(1.15)", "bg": "transparent"},
                        padding="0px",
                    ),
                    href="/",
                ),
                # Buscador conectado al evento set_search_query
                rx.input(
                    placeholder="Buscar cómic...",
                    on_change=ComicsState.set_search_query,
                    bg="#141414",
                    border="1px solid #1e5631",
                    color="white",
                    width="260px",
                    size="2",
                ),
                spacing="3",
                align="center",
            ),
            # Filtros por Editorial
            rx.hstack(
                rx.text(
                    "MARVEL", 
                    font_weight="bold", 
                    color=rx.cond(ComicsState.selected_editorial == "MARVEL", "#00ff66", "white"), 
                    cursor="pointer", 
                    _hover={"color": "#00ff66"},
                    on_click=ComicsState.select_editorial("MARVEL"),
                ),
                rx.text("-", color="#00ff66"),
                rx.text(
                    "DC", 
                    font_weight="bold", 
                    color=rx.cond(ComicsState.selected_editorial == "DC", "#00ff66", "white"), 
                    cursor="pointer", 
                    _hover={"color": "#00ff66"},
                    on_click=ComicsState.select_editorial("DC"),
                ),
                rx.text("-", color="#00ff66"),
                rx.text(
                    "COLABORACIONES", 
                    font_weight="bold", 
                    color=rx.cond(ComicsState.selected_editorial == "COLABORACIONES", "#00ff66", "white"), 
                    cursor="pointer", 
                    _hover={"color": "#00ff66"},
                    on_click=ComicsState.select_editorial("COLABORACIONES"),
                ),
                spacing="3",
                align="center",
            ),
            width="100%",
            justify="between",
            align="center",
            max_width="1200px",
            margin="0 auto",
            padding="10px 20px",
        ),
        bg="#1e5631",
        width="100%",
        border_bottom="2px solid #00ff66",
    )