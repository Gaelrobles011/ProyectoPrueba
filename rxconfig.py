import reflex as rx

config = rx.Config(
    app_name="pagina2",
    plugins=[
        rx.plugins.RadixThemesPlugin(),
        rx.plugins.SitemapPlugin(),
    ],
)
