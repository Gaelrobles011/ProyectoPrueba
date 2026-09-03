import reflex as rx
NAVBAR_LOGO = "/images/T1.png"
def navbar() -> rx.Component:
    return rx.hstack(
        # 1. LOGO E ICONO (Tamaño fijo y controlado)
        rx.hstack(
            rx.image(
                src=NAVBAR_LOGO,
                width="35px",
                height="35px",
                border_radius="50%",
                object_fit="cover",
            ),
            # Oculta el texto en pantallas pequeñas (initial: none) y lo muestra en PC (md: block)
            rx.heading(
                "Tienda_Gael",
                size="5",
                color="white",
                weight="bold",
                display={"initial": "none", "md": "block"},
            ),
            align="center",
            spacing="2",
        ),
        rx.spacer(),
        # 2. MENÚ DE NAVEGACIÓN (Alineado y sin empalmar)
        rx.hstack(
            rx.link(
                "Descubre",
                href="#descubre",
                color="white",
                padding={"initial": "0.5em 0.6em", "md": "1em 1.2em"},
                font_size={"initial": "0.75em", "md": "0.95em"},
                _hover={"background_color": "#1b4332", "text_decoration": "none"},
            ),
            # Botón desplegable Contacto
            rx.popover.root(
                rx.popover.trigger(
                    rx.button(
                        "Contacto",
                        color="white",
                        bg="transparent",
                        border_radius="0",
                        padding={"initial": "0.5em 0.6em", "md": "1em 1.2em"},
                        height="auto",
                        font_weight="normal",
                        font_size={"initial": "0.75em", "md": "0.95em"},
                        border_left="1px solid rgba(255, 255, 255, 0.2)",
                        _hover={"background_color": "#1b4332", "cursor": "pointer"},
                    )
                ),
                rx.popover.content(
                    rx.vstack(
                        rx.link(
                            "Enviar WhatsApp",
                            href="https://wa.me/2361100836",
                            is_external=True,
                            color="white",
                            width="100%",
                            padding="0.5em",
                            _hover={"background_color": "#1b4332", "text_decoration": "none"},
                        ),
                        rx.divider(border_color="rgba(255,255,255,0.2)"),
                        rx.link(
                            "Enviar Correo",
                            href="https://workspace.google.com/intl/es-419_mx/gmail/",
                            is_external=True,
                            color="white",
                            width="100%",
                            padding="0.5em",
                            _hover={"background_color": "#1b4332", "text_decoration": "none"},
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    bg="#2d6a4f",
                    border="1px solid rgba(255, 255, 255, 0.2)",
                    padding="0.5em",
                    border_radius="8px",
                ),
                #DESCARGAR______________________________________________________________________________
            ),
            rx.link(
                "Descarga",
                href="/catalogo.pdf",
                is_external=True,
                download="catalogo.pdf",  # <--- Añade esto para forzar la descarga
                color="white",
                padding={"initial": "0.5em 0.6em", "md":"1em 1.2em"},
                font_size={"initial":"0.75em","md":"0.95em" },
                border_left="1px solid rgba(255, 255, 255, 0.2)",
                _hover={"background_color":"#1b4332","text_decoration":"none"},
            ),
            spacing="0",
            align="center",
    ),
        align="center",
        width="100%",
        padding={"initial": "0 0.5em", "md": "0 2em"},
        background_color="#2d6a4f",
        position="sticky",
        top="0",
        z_index="1000",
        box_sizing="border-box",
)
