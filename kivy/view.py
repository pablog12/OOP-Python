from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class PyCalcUi():
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Create the layout
        self.main_layout = BoxLayout(orientation="vertical")
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        self.display = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        self.main_layout.add_widget(self.display)
    
    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        # Button text | position on the h_layout
        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for btnText in row:
                self.buttons[btnText] = Button(
                    text=btnText,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                h_layout.add_widget(self.buttons[btnText])
            self.main_layout.add_widget(h_layout)
   
    def setDisplayText(self, text):
        """Set display's text."""
        self.display.text = text

    def displayText(self):
        """Get display's text."""
        return self.display.text

    def clearDisplay(self, instance):
        """Clear the display."""
        self.display.text = ""