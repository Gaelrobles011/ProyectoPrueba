import reflex as rx
from pagina2.state.comics_state import ComicsState

def comic_card(comic: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(
                    src=comic["portada"],
                    width="100%",
                    height="260px",
                    object_fit="cover",
                    border_radius="6px",
                ),
                rx.badge(
                    comic["badge"],
                    color_scheme="green",
                    position="absolute",
                    top="8px",
                    left="8px",
                ),
                position="relative",
                width="100%",
            ),
            rx.vstack(
                rx.text(comic["titulo"], font_weight="bold", color="white", no_of_lines=1),
                rx.text(comic["editorial"], font_size="sm", color="#00ff66"),
                rx.hstack(
                    rx.text(comic["precio"], font_size="lg", font_weight="bold", color="white"),
                    rx.spacer(),
                    width="100%",
                ),
                rx.hstack(
                    rx.button(
                        "Añadir",
                        bg="#1e5631",
                        color="white",
                        _hover={"bg": "#2e8b46"},
                        size="2",
                        width="100%",
                    ),
                    rx.button(
                        "Ver",
                        variant="outline",
                        color_scheme="gray",
                        size="2",
                        # Ajuste con lambda para capturar el cómic de la iteración
                        on_click=lambda: ComicsState.open_comic_details(comic),
                    ),
                    width="100%",
                ),
                align_items="start",
                width="100%",
                spacing="2",
            ),
            spacing="3",
            padding="12px",
        ),
        bg="#141414",
        border="1px solid #1e5631",
        border_radius="8px",
        _hover={
            "border_color": "#00ff66",
            "transform": "translateY(-4px)",
            "transition": "all 0.2s ease-in-out",
        },
        width="100%",
    )

def comic_detail_modal() -> rx.Component:
    """Modal emergente protegido contra KeyErrors mediante rx.cond."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.cond(
                ComicsState.is_modal_open,
                rx.hstack(
                    rx.image(
                        src=ComicsState.selected_comic["portada"],
                        width="200px",
                        height="300px",
                        object_fit="cover",
                        border_radius="8px",
                    ),
                    rx.vstack(
                        rx.dialog.title(ComicsState.selected_comic["titulo"], color="white", font_size="xl"),
                        rx.badge(ComicsState.selected_comic["editorial"], color_scheme="green"),
                        rx.hstack(
                            rx.text("Autor: ", font_size="sm", color="gray.400", font_weight="bold"),
                            rx.text(ComicsState.selected_comic["autor"], font_size="sm", color="gray.400"),
                            spacing="1",
                        ),
                        rx.text(ComicsState.selected_comic["sinopsis"], color="gray.300", font_size="sm", margin_top="10px"),
                        rx.heading(ComicsState.selected_comic["precio"], color="#00ff66", size="6", margin_top="15px"),
                        rx.hstack(
                            rx.button(
                                "Añadir al Carrito",
                                bg="#1e5631",
                                color="white",
                                _hover={"bg": "#2e8b46"},
                            ),
                            rx.button(
                                "Cerrar", 
                                variant="soft", 
                                color_scheme="gray", 
                                on_click=ComicsState.close_modal
                            ),
                            spacing="3",
                            margin_top="20px",
                        ),
                        align_items="start",
                        padding_left="15px",
                    ),
                    align="center",
                ),
                rx.fragment(),
            ),
            bg="#141414",
            border="2px solid #00ff66",
            padding="20px",
            max_width="600px",
        ),
        open=ComicsState.is_modal_open,
        on_open_change=ComicsState.close_modal,
    )

def comics_grid() -> rx.Component:
    return rx.vstack(
        rx.grid(
            rx.foreach(ComicsState.filtered_comics, comic_card),
            columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
            spacing="4",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="20px",
        ),
        comic_detail_modal(),
        width="100%",
    )