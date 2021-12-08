import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QCalendarWidget, QComboBox
from PyQt5.uic import loadUi
import prescription
import add_patient
import patient
import mysql.connector
import check_login
from mysql.connector import Error
from datetime import datetime

host_name = 'localhost'
user_name = 'root'
user_password = ''
db_name = 'test_qr'

def database_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name
            )
        print("MYSQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = database_connection(host_name, user_name, user_password, db_name)

class prescWindow(QDialog):
    def __init__(self):
        super(prescWindow,self).__init__()
        loadUi("qrcodeapp.ui",self)
        self.qrButton.clicked.connect(self.createQR)
        self.patient_id = ''
        self.generated_uuid = ''

    def createQR(self):
        medicine_id = self.medicine_id.text()
        dosage = self.dosage.text()
        dispensed_amount = self.dispensed_amount.text()
        frequency = self.frequency.text()
        
        if prescription.checkMedicineID(connection, medicine_id) == 1:
            condition = True
            self.generated_uuid = prescription.createPrescription(connection, self.patient_id, medicine_id, dosage, dispensed_amount, frequency)
            self.prescPopUpWindow(condition)
        else:
            condition = False
            self.prescPopUpWindow(condition)
    
    def prescPopUpWindow(self, condition):
        prescPopUp = QMessageBox()
        prescPopUp.setWindowTitle("Prescription")
        
        if condition == True:
            prescPopUp.setText("Prescription added successfully")
            prescPopUp.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
            buttonAddAnother = prescPopUp.button(QMessageBox.Yes)
            buttonAddAnother.setText('Add Another')
            prescPopUp.buttonClicked.connect(self.popup_button)
            
            prescPopUp.exec_()
            
        elif condition == False:
            prescPopUp.setIcon(QMessageBox.Critical)
            prescPopUp.setText("Medicine ID not found")
            
            prescPopUp.exec_()
        
    def popup_button(self, i):
        if i.text() == 'Add Another':
            idWindow = privIDWindow()
            widget.addWidget(idWindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            qrWindow = QRPhotoWindow()
            qrWindow.generated_uuid = self.generated_uuid
            widget.addWidget(qrWindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
            print(qrWindow.generated_uuid)
        
class privIDWindow(QDialog):
    def __init__(self):
        super(privIDWindow, self).__init__()
        loadUi("patientid.ui", self)
        self.checkIDButton.clicked.connect(self.checkPrivID)
        self.mainMenuButton.clicked.connect(self.returnMainMenu)

    def openMedicineWindow(self, patient_id):
        medWindow = prescWindow()
        medWindow.patient_id = patient_id
        widget.addWidget(medWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def checkPrivID(self):
        patient_id = self.patient_id.text()
        if prescription.checkPatientID(connection,patient_id) == 1:
            condition = True
            self.popUpPrivIDWindow(condition, patient_id)
        else:
            condition = False
            self.popUpPrivIDWindow(condition, patient_id)
    
    def popUpPrivIDWindow(self, condition, patient_id):
        privIDWindowPopUp = QMessageBox()
        privIDWindowPopUp.setWindowTitle("Private ID")
        
        if condition == True:
            privIDWindowPopUp.setText("Patient ID exists")
            privIDWindowPopUp.buttonClicked.connect(lambda:self.openMedicineWindow(patient_id))
            privIDWindowPopUp.exec_()
        elif condition == False:
            privIDWindowPopUp.setIcon(QMessageBox.Critical)
            privIDWindowPopUp.setText("Patient ID does not exist")
            privIDWindowPopUp.buttonClicked.connect(self.addPatientPopUp)
            privIDWindowPopUp.exec_()
            
    def addPatientPopUp(self):
        addPatientWindow = addPatient()
        widget.addWidget(addPatientWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def returnMainMenu(self):
        mainmenuWindow = MainMenu()
        widget.addWidget(mainmenuWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class addPatient(QDialog):
    def __init__(self):
        super(addPatient, self).__init__()
        loadUi("addpatient.ui", self)
        self.addPatientButton.clicked.connect(self.addPatient)
        
    def addPatient(self):
        new_first_name = self.first_name.text()
        new_last_name = self.last_name.text()
        new_sex = self.sex.text()
        new_age = self.age.text()
        new_email = self.email.text()
        new_contactNumber = self.contactNumber.text()
        
        retrieved_info = (new_first_name, new_last_name, new_age, new_sex, new_email, new_contactNumber)
        
        add_patient.addPatientQuery(connection, retrieved_info)
        
        if add_patient.checkPatientIfAdded(connection, retrieved_info) == 1:
            msg = QMessageBox()
            msg.setWindowTitle('Add Patient')
            msg.setText("Add Patient Successfully")
            msg.buttonClicked.connect(self.openCheckPrivWindow)
            msg.exec_() 
        else:
            print("Not added")
            
    def openCheckPrivWindow(self):
        openPrivIDWindow = privIDWindow()
        widget.addWidget(openPrivIDWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class QRPhotoWindow(QDialog):
    def __init__(self):
        super(QRPhotoWindow, self).__init__()
        loadUi("qrphoto.ui", self)
        self.generated_uuid = ''
        self.qrPhotoButton.clicked.connect(self.showImage)
        self.returnButton.clicked.connect(self.returntoPrivWindow)
        
    def showImage(self):
        image_stored = QPixmap("QR Code/"+self.generated_uuid+".png")
        self.qrPhoto.setPixmap(image_stored)
         
    def returntoPrivWindow(self):
        idWindow = privIDWindow()
        widget.addWidget(idWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class userLoginWindow(QDialog):
    def __init__(self):
        super(userLoginWindow, self).__init__()
        loadUi("user_login.ui", self)
        self.loginButton.clicked.connect(self.loginUser)
        self.user_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.credentials = []
        
    def loginUser(self):
        if "patient" in self.user_name.text():
            self.credentials = [int(self.user_name.text().split("_")[1]),self.user_name.text(), self.user_password.text()]
            
            login_result = check_login.checkPatientLogin(connection, self.credentials)
            self.popUpLoginWindow(login_result)
        elif "admin" in self.user_name.text():
            self.credentials = [self.user_name.text(), self.user_password.text()]
            
            login_result = check_login.checkAdminLogin(connection, self.credentials)
            self.popUpLoginWindow(login_result)
    
    def popUpLoginWindow(self, login_result):
        loginPopUp = QMessageBox()
        loginPopUp.setWindowTitle("Login")
        
        if login_result == 1:
            loginPopUp.setText("Successfully logged in!")
            loginPopUp.buttonClicked.connect(self.openMainMenu)
            loginPopUp.exec_()
        elif login_result == 0:
            loginPopUp.setIcon(QMessageBox.Critical)
            loginPopUp.setText("Unsuccessful Login")
            loginPopUp.exec_()
        elif login_result == 2:
            loginPopUp.setText("Successfully logged in!")
            loginPopUp.buttonClicked.connect(self.openpatientWindow)
            loginPopUp.exec_()
            
    def openMainMenu(self):
        mainmenuWindow = MainMenu()
        widget.addWidget(mainmenuWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def openpatientWindow(self):
        patientWindow = patientMenu(self.credentials[0])
        widget.addWidget(patientWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class MedicineMenu(QDialog):
    def __init__(self):
        super(MedicineMenu, self).__init__()
        loadUi("medicine_menu.ui", self)
        self.medicineButton.clicked.connect(self.findMedicine)
        self.mainMenuButton.clicked.connect(self.returnMainMenu)
        
    def findMedicine(self):
        medicine_id = self.medicine_id.text()

        final_data = [index.replace('\r\n', '') for index in prescription.findMedData(connection, medicine_id)]
        
        self.medicine_nameText.setPlainText(final_data[0])
        self.medicine_descText.setPlainText(final_data[1])
        
    def returnMainMenu(self):
        mainmenuWindow = MainMenu()
        widget.addWidget(mainmenuWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class MainMenu(QDialog):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("main_menu.ui", self)
        self.findPatientIDButton.clicked.connect(self.findPatientID)
        self.findMedicineButton.clicked.connect(self.findMedicine)
        
    def findPatientID(self):
        idWindow = privIDWindow()
        widget.addWidget(idWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def findMedicine(self):
        medWindow = MedicineMenu()
        widget.addWidget(medWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class patientMenu(QDialog):
    def __init__(self, patient_id):
        super(patientMenu, self).__init__()
        loadUi("patient_window.ui", self)
        self.patient_id = 0
        self.findName(patient_id)
        self.patient_data = []
        self.findDoctorButton.clicked.connect(self.findDoctors)
        self.reserveSlotButton.clicked.connect(self.reserveSlot)
        self.chosen_doctor = ''
        self.date_selected = ''

    def findName(self, patient_id):
        self.patient_id = patient_id
        data = patient.findPatientName(connection, self.patient_id)
        self.name_label.setText(data[0])
        self.patient_data = data[1]        

    def findDoctors(self):
        self.DoctorNameComboX.clear()
        date = self.calendarWidget.selectedDate()
        weekday = str(date.toPyDate().strftime('%A'))
        self.date_selected = str(date.toPyDate())
        doctors = patient.findDoctor(connection, weekday)

        for i in doctors:
            self.DoctorNameComboX.addItem(i)

        
    def reserveSlot(self):
        self.chosen_doctor = str(self.DoctorNameComboX.currentText())
        
        reservePopUp = QMessageBox()
        reservePopUp.setWindowTitle("Reservation")
        reservePopUp.setText("Choose online or offline appointment for Dr. "+self.chosen_doctor)
        reservePopUp.setStandardButtons(QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        buttonOnline = reservePopUp.button(QMessageBox.Yes)
        buttonOnline.setText('Online')
        buttonOffline = reservePopUp.button(QMessageBox.No)
        buttonOffline.setText('Offline')
        reservePopUp.buttonClicked.connect(self.popup_button)
        
        reservePopUp.exec_()

    def popup_button(self, i):
        if i.text() == "Online":
            patient.slotReservation(connection, "Online", self.chosen_doctor, str(self.date_selected))

            finalPopup = QMessageBox()
            finalPopup.setWindowTitle("Reservation")
            finalPopup.setText("Your appointment with Dr. "+self.chosen_doctor+"for the date "+str(datetime.strptime(self.date_selected, '%Y-%m-%d').strftime('%d-%m-%Y')+" has been booked."))
            finalPopup.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
            buttonAddAnother = finalPopup.button(QMessageBox.Yes)
            buttonAddAnother.setText('Add Another')

            finalPopup.exec_()

        elif i.text() == "Offline":
            patient.slotReservation(connection, "Offline", self.chosen_doctor, str(self.date_selected))

app = QApplication(sys.argv)
mainwindow=userLoginWindow()
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(453)
widget.setFixedWidth(463)
widget.addWidget(mainwindow)
widget.show()
app.exec_()        

