import uuid
import qrcode
from datetime import datetime

def addComma(string):
    new_string = "'"+string+"'"
    return new_string

def createPrescription(connection, patientID, medicine_id, dosage, dispensed_amount, frequency):
    cursor = connection.cursor()
    patient_id = patientID
    generated_uuid = str(uuid.uuid4())
    order_date = str(datetime.today())
    
    prescription_desc = (generated_uuid, patient_id, medicine_id, order_date, dispensed_amount, frequency, dosage)
    map(addComma, prescription_desc)
    
    createPrescription_Query = """INSERT INTO `prescription` (`univ_uniq_identifier`,
                            `patient_id`,
                            `medicine_id`,
                            `order_date`,
                            `dispense_amount`,
                            `frequency`,
                            `dosage`)""" + " VALUES " + str(prescription_desc)
    
    cursor.execute(createPrescription_Query)
    connection.commit()

    generateQR(generated_uuid)
    
    return generated_uuid

def checkPatientID(connection, patientID):
    cursor = connection.cursor()
    checkPatient_Query = """SELECT * FROM `patient` WHERE patient_id="""+str(patientID)+";"
    cursor.execute(checkPatient_Query)
    rows = cursor.fetchall()
    
    if not rows:
        return 0
    else:
        return 1

def checkMedicineID(connection, medicineID):
    cursor = connection.cursor()
    checkPatient_Query = """SELECT * FROM `medicine` WHERE medicine_id="""+str(medicineID)+";"
    cursor.execute(checkPatient_Query)
    rows = cursor.fetchall()
    
    if not rows:
        return 0
    else:
        return 1

def findMedData(connection, medicineID):
    cursor = connection.cursor()
    checkPatient_Query = """SELECT medicine_name, medicine_description FROM `medicine` WHERE medicine_id="""+str(medicineID)+";"
    cursor.execute(checkPatient_Query)
    rows = cursor.fetchall()
    parse_rows = list(rows.pop())
    
    return parse_rows

def generateQR(uuid):
    resource_path = "C:/Users/Aldrian/Documents/4th year/Stratehon/QR Code"
    img = qrcode.make(uuid)
    img.save(resource_path+"/"+str(uuid)+".png")








    
    
    

        


                            
    
    