# import qt_auto as qt
import qt_all as qt
# import qt


class TestWidget(qt.QWidget):
    def __init__(self):
        super().__init__()

        self.button = qt.QPushButton()

        self.vboxlayout = qt.QVBoxLayout(self)
        self.vboxlayout.addWidget(self.button)

    def resizeEvent(self, event: qt.QResizeEvent):
        super().resizeEvent(event)


if __name__ == '__main__':
    def main():
        app = qt.QApplication([])
        test_widget = TestWidget()
        test_widget.show()
        app.exec()

    main()
