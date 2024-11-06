from MainWindow import Ui_MainWindow


class MainwindowExt (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonCalculate.clicked.connect(self.CalculateBMI)

    def showWindow(self):
        self.MainWindow.show()
    def CalculateBMI(self):
        weight = float(self.lineEdiWeight.text())
        height = float(self.lineEditHeight.text())
        height = height / 100
        BMI = weight / (height * height)
        BMI = round(BMI, 2)
        comment = ""
        if BMI < 16:
            comment = "Severe Thinness"
        elif BMI < 17:
            comment = "Moderate Thinness"
        elif BMI < 18.5:
            comment = "Mild Thinness"
        elif BMI < 25:
            comment = "Normal"
        elif BMI < 30:
            comment = "Overweight"
        elif BMI < 35:
            comment = "Obese Class I"
        elif BMI < 40:
            comment = "Obese Class II"
        else:
            comment = "Obese Class III"
        self.labelBMI.setText(str(BMI))
        self.labelComment_2.setText(comment)