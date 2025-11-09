"""
Internationalization and localization support.
"""

from utils import dataclass, app, PreloadJs, field


@dataclass
class I18N(PreloadJs):
    """Internationalization based on PreloadJs."""
    path: str = field(init=False)

    def __post_init__(self) -> None:
        lang = app.config.get_param("app", "language")
        self.path = f"locales/{lang}"
        super().__post_init__()

    def switch(self) -> None:
        """Switch the language and reload the JSON."""
        self.__post_init__()

i18n = I18N()
