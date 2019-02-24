def new_password (oldpassword, newpassword):
    if oldpassword == newpassword or len(str(newpassword)) < 6:
        return 'False'
    else:
        return 'True'
