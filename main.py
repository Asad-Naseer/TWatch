from textual.app import App, on # the class from textual that our app needs to inherit from
from textual.widgets import Header, Footer, Button, Static
from my_widgets import Custom_timer, Stopwatch


class StopwatchApp(App):
    
    CSS_PATH = "./stopwatch.css"

    BINDINGS = [
                # ("keybind", "action_name", "label")
                ("d", "toggle_dark_mode", "Toggle Dark Mode"),
                ("t", "set_theme", "Select Themes")
            ]

    def compose(self):
        yield Header(icon="")
        yield Footer(show_command_palette=False)
        yield Stopwatch()
        yield Stopwatch()
        self.theme = 'catppuccin-frappe'

    def action_toggle_dark_mode(self):
       self.theme = "solarized-light" if self.theme == "catppuccin-frappe" else "catppuccin-frappe"

    def action_set_theme(self):
        self.search_themes()


if __name__ == "__main__":
    StopwatchApp().run()