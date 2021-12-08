def checkPatientLogin(connection, credentials):
    cursor = connection.cursor()
    print(credentials)
    if "admin" in credentials[1]:
        checkLogin_Query = """SELECT * FROM `user_login` WHERE user_id="""+'"'+credentials[1]+'"'+";"
    
    elif "patient" in credentials[1]:
        checkLogin_Query = """SELECT * FROM `patient_login` WHERE patient_user="""+'"'+credentials[1]+'"'+";"
    
    cursor.execute(checkLogin_Query)
    result = cursor.fetchall()
    parse_result = list(result.pop())
    
    if credentials == parse_result:
        if "admin" in credentials[1]:
            return 1
        elif "patient" in credentials[1]:
            return 2
    else:
        return 0
    
def checkAdminLogin(connection, admin_credentials):
    cursor = connection.cursor()
    
    checkLogin_Query = """SELECT * FROM `user_login` WHERE user_id="""+'"'+admin_credentials[0]+'"'+";"
    
    cursor.execute(checkLogin_Query)
    result = cursor.fetchall()
    parse_result = list(result.pop())
    
    if admin_credentials == parse_result:
        return 1
    else:
        return 0
    
    