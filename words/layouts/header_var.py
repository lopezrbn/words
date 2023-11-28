import reflex as rx
from datetime import datetime

from words.state import State
from words.styles.styles import Size


def header_var() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.image(src="/main-logo-transparent.png"),
                href="./home",
            ),
            rx.heading(
                State.date_today,
                font_size= Size.MEDIUM_BIG.value,
            ),
            align_items="center",
        ),
        rx.divider(),
    )