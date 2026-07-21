import sys

from decimal import Decimal

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QLCDNumber, QLayoutItem, \
    QSizePolicy, QLabel


class Calculator(QMainWindow):

    def __init__(self)->None:

        super().__init__()
        self.setWindowTitle('Calculator')
        self.resize(400, 500)
        self.setStyleSheet("background: #36363A")

        self.value = "0" # Base value of the screen
        self.calculType = "None" # Type of calcul chose to make the operation
        self.lastValue = "0" # Memorize the first value of an operation
        self.memory = 0 # Memory for M button
        self.resetValue = False # Flag for reset the value after the final result apparition

        self.createWidget()
        self.createLayout()
        self.createStyle()
        self.createSignals()

    def createWidget(self)->None:

        self.screen = QLCDNumber()

        self.buttonSeven = QPushButton("7")
        self.buttonEight = QPushButton("8")
        self.buttonNine = QPushButton("9")
        self.buttonFour = QPushButton("4")
        self.buttonFive = QPushButton("5")
        self.buttonSix = QPushButton("6")
        self.buttonOne = QPushButton("1")
        self.buttonTwo = QPushButton("2")
        self.buttonThree = QPushButton("3")
        self.buttonZero = QPushButton("0")

        self.buttonMc = QPushButton("MC")
        self.buttonMPlus = QPushButton("M+")
        self.buttonMMinus = QPushButton("M-")
        self.buttonMr = QPushButton("MR")
        self.buttonC = QPushButton("C")
        self.buttonCE = QPushButton("CE")

        self.buttonDivision = QPushButton("÷")
        self.buttonMultiplication = QPushButton("x")
        self.buttonMinus = QPushButton("-")
        self.buttonPlus = QPushButton("+")
        self.buttonEqual = QPushButton("=")
        self.buttonPoint = QPushButton(".")
        self.buttonPlusOrMinus = QPushButton("+/-")
        self.buttonModulo = QPushButton("%")
        self.buttonDivisionInt = QPushButton("÷R")
        self.buttonSquareRoot = QPushButton("√")

        self.calculatorLabel = QLabel("Calculator")
        self.calculatorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.calculatorLabel.setScaledContents(True)

    def createLayout(self)->None:

        self.grid = QGridLayout()
        self.grid.addWidget(self.screen, 0, 0, 1, 5)
        self.grid.addWidget(self.buttonMc, 2, 0)
        self.grid.addWidget(self.buttonMPlus, 2, 2)
        self.grid.addWidget(self.buttonDivision, 1, 4)
        self.grid.addWidget(self.buttonMultiplication, 2, 4)
        self.grid.addWidget(self.buttonSeven, 3, 1)
        self.grid.addWidget(self.buttonEight, 3, 2)
        self.grid.addWidget(self.buttonNine, 3, 3)
        self.grid.addWidget(self.buttonMinus, 3, 4)
        self.grid.addWidget(self.buttonFour, 4, 1)
        self.grid.addWidget(self.buttonFive, 4, 2)
        self.grid.addWidget(self.buttonSix, 4, 3)
        self.grid.addWidget(self.buttonPlus, 4, 4)
        self.grid.addWidget(self.buttonOne, 5, 1)
        self.grid.addWidget(self.buttonTwo, 5, 2)
        self.grid.addWidget(self.buttonThree, 5, 3)
        self.grid.addWidget(self.buttonEqual, 5, 4, 2, 1)
        self.grid.addWidget(self.buttonZero, 6, 1, 1, 2)
        self.grid.addWidget(self.buttonPoint, 6, 3)
        self.grid.addWidget(self.buttonMr, 2, 1)
        self.grid.addWidget(self.buttonMMinus, 2, 3)
        self.grid.addWidget(self.buttonModulo, 3, 0)
        self.grid.addWidget(self.buttonPlusOrMinus, 4, 0)
        self.grid.addWidget(self.buttonCE, 5, 0)
        self.grid.addWidget(self.buttonC, 6, 0)
        self.grid.addWidget(self.buttonDivisionInt, 1, 3)
        self.grid.addWidget(self.buttonSquareRoot, 1, 2)
        self.grid.addWidget(self.calculatorLabel, 1, 0, 1, 2)

        central_widget = QWidget()
        central_widget.setLayout(self.grid)
        self.setCentralWidget(central_widget)

    def createStyle(self)->None:

        for line in range(7):
            self.grid.setRowStretch(line, 2 if line == 0 else 1)

        for idx in range(self.grid.count()):
            item: QLayoutItem | None = self.grid.itemAt(idx)
            widget = item.widget()
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            if isinstance(widget, QPushButton):
                widget.setStyleSheet("background: #595959; color: white; font-weight: bold; font-size: 20px")
            elif isinstance(widget, QLabel):
                widget.setStyleSheet("background: #36363A; font-weight: bold")
            else:
                widget.setStyleSheet("background: #a2af77; font-weight: bold")

        self.buttonEqual.setStyleSheet("background: #f05a2D; font-weight: bold; font-size: 20px; color: white;")
        self.buttonC.setStyleSheet("background: #F9C210; color: white; font-weight: bold; font-size: 20px")

    def createSignals(self)->None:

        self.buttonSeven.clicked.connect(self.numberButtonClicked)
        self.buttonEight.clicked.connect(self.numberButtonClicked)
        self.buttonNine.clicked.connect(self.numberButtonClicked)
        self.buttonFour.clicked.connect(self.numberButtonClicked)
        self.buttonFive.clicked.connect(self.numberButtonClicked)
        self.buttonSix.clicked.connect(self.numberButtonClicked)
        self.buttonOne.clicked.connect(self.numberButtonClicked)
        self.buttonTwo.clicked.connect(self.numberButtonClicked)
        self.buttonThree.clicked.connect(self.numberButtonClicked)
        self.buttonZero.clicked.connect(self.numberButtonClicked)

        self.buttonPoint.clicked.connect(self.pointButtonClicked)

        self.buttonPlus.clicked.connect(self.setNewCalculType)
        self.buttonMinus.clicked.connect(self.setNewCalculType)
        self.buttonDivision.clicked.connect(self.setNewCalculType)
        self.buttonMultiplication.clicked.connect(self.setNewCalculType)
        self.buttonDivisionInt.clicked.connect(self.setNewCalculType)
        self.buttonModulo.clicked.connect(self.setNewCalculType)

        self.buttonPlusOrMinus.clicked.connect(self.changeValueSign)
        self.buttonSquareRoot.clicked.connect(self.squareRoot)
        self.buttonEqual.clicked.connect(self.result)

        self.buttonCE.clicked.connect(self.clearEntry)
        self.buttonC.clicked.connect(self.clear)

        self.buttonMPlus.clicked.connect(self.memoryAdd)
        self.buttonMMinus.clicked.connect(self.memorySubtract)
        self.buttonMr.clicked.connect(self.memoryDisplay)
        self.buttonMc.clicked.connect(self.memoryReset)

    @Slot()
    def numberButtonClicked(self)->None:

        if self.value == "0" or self.value == 'ERROR' or (self.resetValue == True and self.calculType == 'None'):
            self.value = self.sender().text()
            self.resetValue = False
        else:
            self.value = self.value + self.sender().text()
        self.screenUpdate()


    @Slot()
    def pointButtonClicked(self) -> None:

        value = self.value

        if value == 'ERROR' or (self.resetValue == True and self.calculType == 'None'): # Check if the previous operation was an error or if we need to reset it
            self.value = '0.'
            self.resetValue = False

        if '.' not in value:
            self.value = value + '.'
        self.screenUpdate()


    def screenUpdate(self)->None:

        screenValue = self.value
        n = len(screenValue)
        if n > 5:
            self.screen.setDigitCount(n) # Adapt the max digits number
        else:
            self.screen.setDigitCount(5) # Base display max digits number

        self.screen.display(screenValue) # Display the value

    @Slot()
    def setNewCalculType(self)->None:

        if self.calculType != "None" and self.value != '0': # Look if there is already a calcul in process, and give the possibility to change operating mode if we haven't typed any numbers after it
            self.result()

        self.calculType = self.sender().text() # Update the type of calcul we make
        self.lastValue = self.value # Save the first value for the calcul
        self.value = "0" # The value is reinitialized to zero

    @Slot()
    def result(self)->None:

        if (self.calculType == "÷" or self.calculType == '÷R') and Decimal(self.value) == Decimal(0): # Check if there is division by zero
                self.value = 'ERROR'
        else: # Make the correct operation and remove useless zero from the value (Decimal can take str value)
            value = Decimal(0)
            if self.calculType == "+": # addition
                value = (Decimal(self.value) + Decimal(self.lastValue)).normalize()

            elif self.calculType == "-": # subtraction
                value = (Decimal(self.lastValue) - Decimal(self.value)).normalize()

            elif self.calculType == "x": # multiplication
                value = (Decimal(self.value) * Decimal(self.lastValue)).normalize()

            elif self.calculType == "%": # modulo
                value = (Decimal(self.lastValue) % Decimal(self.value)).normalize()

            elif self.calculType == "÷" and self.value != '0':  # division
                value = (Decimal(self.lastValue) / Decimal(self.value)).normalize()

            elif self.calculType == "÷R" and self.value != '0':  # Euclidean division
                value = (Decimal(self.lastValue) // Decimal(self.value)).normalize()

            else: # Same value, nothing change
                value = Decimal(self.value).normalize()

            self.value = f"{value:f}" # Convert back the value to str

        self.resetValue = True
        self.lastValue = '0' # The last value is reinitialized to zero
        self.calculType = 'None' # Reinitialized calcul type after the operation
        self.screenUpdate() # Update the screen


    @Slot()
    def squareRoot(self)->None:

        if self.lastValue != "0":
            self.result()
        if Decimal(self.value) < Decimal(0): # Reject negative value
            self.value = 'ERROR'
        else:
            self.value = f"{(Decimal(self.value) ** Decimal(1/2)).normalize():f}" # Find the square root, remove useless zero and convert back the value to str

        self.calculType = 'None' # Reinitialized calcul type after the operation
        self.screenUpdate()

    @Slot()
    def changeValueSign(self):

        if self.value[0] == "-": # Take the minus of if there is one already
            self.value = self.value[1:]
        elif self.value != "0":
            self.value = "-" + self.value # Put the minus in front of the value

        self.screenUpdate()  # Update the screen

    @Slot()
    def clearEntry(self)->None:

        self.value = "0" # Reset the current value
        self.screenUpdate()  # Update the screen

    @Slot()
    def clear(self)->None:

        self.value = "0"  # Reset the current value
        self.lastValue = "0" # Reset the last value saved
        self.calculType = "None" # Reset the calcul type
        self.screenUpdate()  # Update the screen

    @Slot()
    def memoryAdd(self)->None:

        if self.calculType != 'None':
            self.result()
        self.memory = (Decimal(self.memory) + Decimal(self.value)).normalize()

    @Slot()
    def memorySubtract(self)->None:

        if self.calculType != 'None':
            self.result()
        self.memory = (Decimal(self.memory) - Decimal(self.value)).normalize()

    @Slot()
    def memoryDisplay(self)->None:

        self.value = str(self.memory)
        self.screenUpdate()

    @Slot()
    def memoryReset(self)->None:

        self.memory = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = Calculator()
    myWindow.show()

    sys.exit(app.exec())
