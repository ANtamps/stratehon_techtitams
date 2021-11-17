def checkLogin(connection, admin_credentials):
    cursor = connection.cursor()
    
    checkLogin_Query = """SELECT * FROM `user_login` WHERE user_id="""+'"'+admin_credentials[0]+'"'+";"
    
    cursor.execute(checkLogin_Query)
    result = cursor.fetchall()
    parse_result = list(result.pop())
    
    if admin_credentials == parse_result:
        return 1
    else:
        return 0
    
    
        
    
    