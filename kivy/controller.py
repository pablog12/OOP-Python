from functools import partial
from model import ERROR_MSG

# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc Controller class."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self, instance):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp, instance):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.bind(on_press=partial(self._buildExpression, btnText))

        self._view.buttons['='].bind(on_press=self._calculateResult)
        self._view.buttons['C'].bind(on_press=self._view.clearDisplay)