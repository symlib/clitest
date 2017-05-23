# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyFc(c):
    FailFlag = False
    tolog("<b>Verify fc </b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyFcList(c):
    FailFlag = False
    tolog("<b>Verify fc -a list</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyFcMod(c):
    FailFlag = False
    tolog("<b>Verify fc -a mod</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyFcReset(c):
    FailFlag = False
    tolog("<b>Verify fc -a reset</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc -a reset </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyFcClear(c):
    FailFlag = False
    tolog("<b>Verify fc -a clear</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc -a clear </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifFcSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify fc specify inexistent Id </b>")
    # -i <ctrlId>  (1,2)
    # -p <port id> (1,4)

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyFcInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify fc invalid option</b>")
    command = ['fc -x', 'fc -a list -x', 'fc -a mod -x', 'fc -a reset -x', 'fc -a clear -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyFcInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify fc invalid parameters</b>")
    command = ['fc test', 'fc -a list test', 'fc -a mod test', 'fc -a reset test', 'fc -a clear test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyFcMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify fc missing parameters</b>")
    command = ['fc -a list -p', 'fc -a mod -i', 'fc -a reset -i', 'fc -a clear -p']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify fc missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyFc(c)
    verifyFcList(c)
    verifyFcMod(c)
    verifyFcReset(c)
    verifyFcClear(c)
    verifFcSpecifyInexistentId(c)
    verifyFcInvalidOption(c)
    verifyFcInvalidParameters(c)
    verifyFcMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped