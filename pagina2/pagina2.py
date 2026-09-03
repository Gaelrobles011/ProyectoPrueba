import reflex as rx
from pagina2.pages.index import index
from pagina2.components.carrusel import carousel
from pagina2.pages.comics import comics


app = rx.App()
app.add_page(index, route="/", title="Gael_WEB")
app.add_page(comics, route="/comics")
