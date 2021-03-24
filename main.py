from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = ""# ENTER RSAKEY
auth = "" ## AUTHKEY WITH ACTIVATE !
def Authkey():
    key = str(input(" Enter Auth Key :-"))
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id='##PRODUCTID##', \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
    else:
    # everything went fine if we are here!
        print("The license is valid!")
        pass
Authkey()
