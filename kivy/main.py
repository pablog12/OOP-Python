from kivy.app import App

from model import evaluateExpression, ERROR_MSG
from view import PyCalcUi
from controller import PyCalcCtrl


class MainApp(App):
    def build(self):
        View = PyCalcUi()

        # Create instances of the model and the controller
        self.main_layout = View.main_layout
        model = evaluateExpression
        PyCalcCtrl(model=model, view=View)

        return self.main_layout


if __name__ == '__main__':
    app = MainApp()
    app.run()