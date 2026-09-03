import asyncio
import reflex as rx

SLIDES = [
    {
        "title": "Tecnologia",
        "image": "/images/tecnologia.jpeg",
    },
    {
        "title": "Videojuegos",
        "image": "/images/videojuegos.jpeg",
    },
    {
        "title": "Mangas",
        "image": "/images/mangas.jpeg",
    },
    {
        "title": "Comics",
        "image": "/images/comics.jpeg",
    },
]


class CarouselState(rx.State):
    current_index: int = 0
    _is_running: bool = False

    def next_slide(self):
        self.current_index = (self.current_index + 1) % len(SLIDES)

    def prev_slide(self):
        self.current_index = (self.current_index - 1 + len(SLIDES)) % len(SLIDES)

    def set_slide(self, index: int):
        self.current_index = index

    @rx.event(background=True)
    async def auto_play(self):
        if CarouselState._is_running:
            return
        CarouselState._is_running = True
        
        while True:
            await asyncio.sleep(3)
            async with self:
                self.next_slide()

    @rx.var
    def current_image(self) -> str:
        return SLIDES[self.current_index]["image"]

    @rx.var
    def current_title(self) -> str:
        return SLIDES[self.current_index]["title"]


def carousel() -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src=CarouselState.current_image,
                width="100%",
                height="100vh",
                object_fit="cover",
                style={
                    "transition": "opacity 0.6s ease-in-out",
                },
            ),
            # Capa oscura para contraste
            rx.box(
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                background="linear-gradient(to top, rgba(5, 11, 8, 0.95) 0%, rgba(5, 11, 8, 0.2) 60%, transparent 100%)",
            ),
            # Título y solo los indicadores de puntos
            rx.vstack(
                rx.heading(
                    CarouselState.current_title,
                    size={"initial": "8", "md": "9"},
                    color="white",
                    weight="bold",
                    style={
                        "text_shadow": "0 2px 10px rgba(0,0,0,0.8)",
                        "transition": "opacity 0.6s ease-in-out",
                    },
                ),
                rx.hstack(
                    *[
                        rx.box(
                            width=rx.cond(
                                CarouselState.current_index == i,
                                "28px",
                                "10px",
                            ),
                            height="10px",
                            border_radius="full",
                            background=rx.cond(
                                CarouselState.current_index == i,
                                "#00FF88",
                                "rgba(255, 255, 255, 0.4)",
                            ),
                            cursor="pointer",
                            on_click=CarouselState.set_slide(i),
                            transition="all 0.3s ease",
                        )
                        for i in range(len(SLIDES))
                    ],
                    spacing="2",
                    align="center",
                    margin_top="1em",
                ),
                align_items="start",
                position="absolute",
                bottom="80px",
                left={"initial": "20px", "md": "60px"},
                spacing="2",
            ),
            position="relative",
            width="100%",
            height="100vh",
        ),
        id="descubre",
        position="sticky",
        top="0",
        z_index="1",
        width="100%",
        on_mount=CarouselState.auto_play,
    )