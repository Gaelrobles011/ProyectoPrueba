import reflex as rx

def tarjeta_item(imagen: str, titulo: str, enlace: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=imagen,
                width="100%",
                height="180px",
                object_fit="cover",
                border_radius="10px 10px 0 0",
            ),
            rx.box(
                rx.text(
                    titulo,
                    color="white",
                    weight="bold",
                    font_size="1.1em",
                    text_align="center",
                ),
                padding="15px",
                width="100%",
            ),
            align_items="center",
            background_color="#1b4332",
            border_radius="10px",
            box_shadow="0 4px 10px rgba(0,0,0,0.3)",
            overflow="hidden",
            transition="transform 0.2s ease",
            _hover={"transform": "translateY(-5px)", "box_shadow": "0 8px 20px rgba(0,0,0,0.5)"},
        ),
        href=enlace,
        is_external=False,
        _hover={"text_decoration": "none"},
    )

def seccion_explora() -> rx.Component:
    return rx.vstack(
        # Cuadrícula de 4 tarjetas responsivas sin fondo extra
        rx.grid(
            tarjeta_item("/images/co4.jpeg", "Cómics de Colección", "/comics"),  # <-- ¡Aquí cambió a "/comics"!
            tarjeta_item("/images/tec1.jpeg", "Tecnología y Gadgets", "#tecnologia"),
            tarjeta_item("/images/man3.jpeg", "Mangas Populares", "#mangas"),
            tarjeta_item("/images/ju2.jpeg", "Videojuegos", "#videojuegos"),
            columns={"initial": "1", "sm": "2", "md": "4"},
            spacing="5",
            width="100%",
            padding={"initial": "1em", "md": "1em 0"},
        ),
        width="100%",
        background_color="transparent",  # Fondo transparente para usar el negro de tu index
        padding_top="10px",
        padding_bottom="20px",
        id="descubre",
    )