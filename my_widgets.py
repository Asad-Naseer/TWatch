from textual.widgets import Header, Footer, Button, Static
from textual import on

class Custom_timer(Static):
    """Simple timer widget"""
    pass


class Stopwatch(Static):
    """Custom Stopwatch widget"""
    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")

    def compose(self):
        yield Button("Start", classes="trans", id="start")   
        yield Button("Stop", classes="trans hidden", id="stop")
        yield Button ("Reset", classes="trans", id="reset")
        yield Custom_timer("00:00:00.00", id="timer")

