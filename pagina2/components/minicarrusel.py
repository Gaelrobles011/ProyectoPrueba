import reflex as rx

def tarjeta_simple(texto: str) -> rx.Component:
    return rx.center(
        rx.text(texto, color="white", font_weight="bold", font_size="0.9em", text_align="center"),
        width="220px",
        height="110px",
        background_color="#07330E",
        border_radius="12px",
        padding="15px",
    )

def mini_carrusel() -> rx.Component:  # <--- Mantén este nombre aquí
    frases = [
        "Animate a Leer",
        "Explora Mundos",
        "Conectate con la Tecnologia"
    ]

    return rx.hstack(
        *[tarjeta_simple(f) for f in frases],
        spacing="4",
        align="center",
        justify="center",
        width="100%",
    )