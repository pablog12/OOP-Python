# Creating a Calculator With Python and PyQt

In this section, you’re going to develop a calculator using the Model-View-Controller (MVC) design pattern. This pattern has three layers of code, each with different roles:

The model takes care of your app’s business logic. It contains the core functionality and data. For your calculator, the model will handle the calculations.

The view implements your app’s GUI. It hosts all the widgets the end-user would need to interact with the application. The view also receives user actions and events. For your calculator, the view will be the window you’ll see on your screen.

The controller connects the model and the view to make the application work. User events (or requests) are sent to the controller, which puts the model to work. When the model delivers the requested result (or data) in the right format, the controller forwards it to the view. For your calculator, the controller will receive user events from the GUI, ask the model to perform calculations, and update the GUI with the result.

Here’s a step-by-step MVC pattern for a GUI desktop application:

* The user performs an action or request (event) on the view (GUI).
* The view notifies the controller about the user’s action.
* The controller gets the user’s request and queries the model for a response.
* The model processes the controller query, performs the required operations, and returns an answer or result.
* The controller receives the model’s answer and updates the view accordingly.
* The user finally sees the requested result on the view.
* You’ll use this MVC design pattern to build your calculator.

`https://realpython.com/python-pyqt-gui-calculator/`