import os
import validation

datapath = "acclog/records/"
def create(account_number, first_name, last_name, email, password):
    created = False
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if os.path.exists(datapath + str(account_number) + ".txt"):
        print("User already exists")
        return False
    else:
        try:
            f = open(datapath + str(account_number) + ".txt", "x")
        except FileExistsError:
            print("Account already exist")
        else:
            f.write(str(user_data))
            created = True
        finally:
            f.close()
            return created

def read(account_number):
    valid_user_acc = validation.account_validation(account_number)
    try:
        if valid_user_acc:
            f = open(datapath + str(account_number) + ".txt")
        else:
            f = open(datapath + str(account_number))
    except FileNotFoundError:
        print("Not found")
    except FileExistsError:
        print("User not found")
    except TypeError:
        print("error")
    finally:
        return f.readline()

def does_account_number_exist(account_number):

    all_users = os.listdir(datapath)

    for user in all_users:

        if user == str(account_number) + ".txt":

            return True

    return False

def authenticated_user(account_number, password):

    user = str.split(read(account_number), ',')

    if password == user[3]:
        return user

def update(account_number, user):
    user_data = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + user[4]
    try:
        f = open(datapath + str(account_number) + ".txt", "w")
    except:
        print("not updated")
    else:
        f.write(str(user_data))


#def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true
