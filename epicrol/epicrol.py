"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from epicrol.components.navbar import navbar
from epicrol.components.message import message
from epicrol.components.send_bar import send_bar
from epicrol.styles.colors import Color

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            message(avatar="avatar_ex.jpg", name="Lolita", text_m="No me toques las orejas que me pongo tontorrona."),
            margin="1em",
            height="80%",
        ),
        send_bar(),
        margin_top ="2em",
        bg =Color.CELESTE.value,
     )

app = rx.App()
app.add_page(index)
