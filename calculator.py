
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def zero ( ):
    global number
    number = number + "0" 
    window.textbox.setText (number)

def one ():
    global number
    number = number + "1"
    window.textbox.setText (number)

def two () :
    global number
    number = number + "2"
    window.textbox.setText (number)

def three () :
    global number
    number = number + "3"
    window.textbox.setText (number)

def four () :
    global number
    number = number + "4"
    window.textbox.setText (number)

def five () :
    global number
    number = number + "5"
    window.textbox.setText (number)

def six () :
    global number
    number = number + "6"
    window.textbox.setText (number)

def seven () :
    global number
    number = number + "7"
    window.textbox.setText (number)

def eight () :
    global number 
    number = number + "8"
    window.textbox.setText (number)

def nine () :
    global number
    number = number + "9"
    window.textbox.setText (number)

def ac () :
    global number 
    number = ""
    window.textbox.setText (number)

def sum () :
    global number
    global operation
    global first
    first = int ( number )
    operation = "+"
    number = ""
    window.textbox.setText (number)

def equal () :
    global number
    global first
    global operation
    second = int ( number )

    if operation == "+" :
        result = first + second
    
    window.textbox.setText (str(result))
    number = ""
    operation = ""
    first = ""


app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("calculator.ui")
number = ""
operation = ""

window.zero.clicked.connect (zero)
window.one.clicked.connect (one)
window.two.clicked.connect (two)
window.three.clicked.connect (three)
window.four.clicked.connect (four)
window.five.clicked.connect (five)
window.six.clicked.connect (six)
window.seven.clicked.connect (seven)
window.eight.clicked.connect (eight)
window.nine.clicked.connect (nine)

window.equal.clicked.connect (equal)
window.sum.clicked.connect (sum)

window.ac.clicked.connect (ac)

window.show ()
app.exec ()