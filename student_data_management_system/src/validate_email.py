def check_email(mail):
    """This function will check 
    whether input email is valid or 
    invalid format

    Args:
        mail (str): input string as mail

    Returns:
        bool: True if format of email is valid
    """
    digits = "0123456789"
    valid_symbol = "@."
    bool_isvalid = True
    if  ('@' in mail) and (mail.count('@') == 1):
        if len(mail)>=6 or len(mail)<=40:
            if (mail[-3] == '.') ^ (mail[-4] =='.'):
                    for i in mail:
                        if (i in digits) or (i in valid_symbol):
                            continue
                        if i != " ":    
                            if i == i.upper():
                                bool_isvalid = False
                                break
                        else:
                            bool_isvalid = False
                            break 
            else:
                bool_isvalid = False
        else:
            bool_isvalid = False
    else:
       bool_isvalid = False

    return bool_isvalid

if __name__ == "__main__":
    mail = "lasiwasumit@gmail.com"
    print(check_email(mail))






