# Build a PyQt application with a QTabWidget containing multiple tabs. Each tab should
# have different content, such as text, buttons, or images.

import sys
from PyQt5.QtWidgets import (
QApplication,
QVBoxLayout,
QPushButton,
QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        self.setGeometry(300, 300, 400, 200)
        
        # Create a QHBoxLayout instance
        layout = QVBoxLayout()
        
        # Add widgets to the layout
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        
        # Set the layout on the application's window
        self.setLayout(layout)
        print(self.children())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())