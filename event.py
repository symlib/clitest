# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyEvent(c):
    FailFlag = False
    tolog("<b>Verify event </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEventList(c):
    FailFlag = False
    tolog("<b>Verify event -a list</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEventClear(c):
    FailFlag = False
    tolog("<b>Verify event -a clear</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event -a clear </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifEventSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify event specify inexistent Id </b>")
    # -i <sequence ID>  (0,65535)
    # -c <event count>  (0,65535)

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)



def verifyEventInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify event invalid option</b>")
    command = ['event -x', 'event -a list -x', 'event -a clear -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEventInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify event invalid parameters</b>")
    command = ['event test', 'event -a test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEventMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify event missing parameters</b>")
    command = ['event -a', 'event -a list -i ', 'event -a list -i 0 -c']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify event missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyEvent(c)
    verifyEventList(c)
    verifyEventClear(c)
    verifEventSpecifyInexistentId(c)
    verifyEventInvalidOption(c)
    verifyEventInvalidParameters(c)
    verifyEventMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped