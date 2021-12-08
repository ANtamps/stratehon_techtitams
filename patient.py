def addComma(string):
    new_string = "'"+string+"'"
    return new_string

def findPatientName(connection, patientID):
    cursor = connection.cursor()
    checkPatient_Query = """SELECT * FROM `patient` WHERE patient_id="""+str(patientID)+";"
    cursor.execute(checkPatient_Query)
    rows = cursor.fetchall()
    
    patient_data = list(rows[0])
    name = patient_data[1]+" "+patient_data[2]

    return name, patient_data

def findDoctor(connection, weekday):
    cursor = connection.cursor()
    weekday_query = addComma(weekday)
    checkDoctor_Query = "SELECT doctor_name FROM `doctor` WHERE (doctor_date1="+weekday_query+" OR doctor_date2="+weekday_query+" OR doctor_date3="+weekday_query+");"
    cursor.execute(checkDoctor_Query)
    rows = cursor.fetchall()
   
    doctors = []

    for doctor_names in rows:
        doctors.append(list(doctor_names).pop())
    
    return doctors

def slotReservation(connection, state, chosen_doctor, date_selected):
    cursor = connection.cursor()
    checkDoctor_Query = "SELECT doctor_id FROM `doctor` WHERE (doctor_name="+addComma(chosen_doctor)+");"
    cursor.execute(checkDoctor_Query)
    rows = cursor.fetchall()
    
    doctor_id = list(rows.pop())[0]

    if state=="Online":
        state=1
    elif state=="Offline":
        state=0

    appointment_list = (doctor_id, date_selected, state)
    map(addComma, appointment_list)

    makeAppointment_Query = """INSERT INTO `appointment`(
                                                        `doctor_id`, 
                                                        `appointment_date`, 
                                                        `isOnline`)""" + " VALUES " + str(appointment_list)

    cursor.execute(makeAppointment_Query)
    connection.commit()