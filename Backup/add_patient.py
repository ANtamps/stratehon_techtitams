def addComma(string):
    new_string = "'"+string+"'"
    return new_string

def addPatientQuery(connection, retrieved_info):
    cursor = connection.cursor()
    patient_desc = retrieved_info
    map(addComma, patient_desc)
    
    addPatient_Query = """INSERT INTO `patient` (`patient_first_name`,
                            `patient_last_name`,
                            `patient_age`,
                            `patient_sex`,
                            `patient_email`,
                            `patient_contact_number`)""" + " VALUES " + str(patient_desc)

    cursor.execute(addPatient_Query)
    connection.commit()
    
def checkPatientIfAdded(connection, retrieved_info):
    cursor = connection.cursor()
    patient_name = '"'+retrieved_info[0]+'"'
    checkPatient_Query = """SELECT EXISTS(SELECT 1 FROM `patient` WHERE patient_first_name="""+str(patient_name)+");"
    
    cursor.execute(checkPatient_Query)
    result = cursor.fetchone()
    
    if not result:
        return 0
    else:
        return 1

    

    