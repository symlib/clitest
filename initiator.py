# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyInitiator(c):
    FailFlag = False
    tolog("<b>Verify initiator </b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorList(c):
    FailFlag = False
    tolog("<b>Verify initiator -a list</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorAdd(c):
    FailFlag = False
    tolog("<b>Verify initiator -a add </b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator -a add </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorDel(c):
    FailFlag = False
    tolog("<b>Verify initiator -a del</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator -a del </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify initiator specify inexistent Id </b>")
    # -i <Index> (0,2047)

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyInitiatorInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify initiator invalid option</b>")
    command = ['initiator -x', 'initiator -a list -x', 'initiator -a add -x', 'initiator -a del -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyInitiatorInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify initiator invalid parameters</b>")
    command = ['initiator test', 'initiator -a list test', 'initiator -a add test', 'initiator -a del test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyInitiatorMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify initiator missing parameters</b>")
    command = ['initiator -i', 'initiator -a list -i', 'initiator -a add -i', 'initiator -a del -i']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyInitiator(c)
    verifyInitiatorList(c)
    verifyInitiatorAdd(c)
    verifyInitiatorDel(c)
    verifyInitiatorSpecifyInexistentId(c)
    verifyInitiatorInvalidOption(c)
    verifyInitiatorInvalidParameters(c)
    verifyInitiatorMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped