# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyBattery(c):
    FailFlag = False
    tolog("<b>Verify battery </b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatteryList(c):
    FailFlag = False
    tolog("<b>Verify battery -a list</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatteryRecondition(c):
    FailFlag = False
    tolog("<b>Verify battery -a recondition</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery -a recondition</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatterySpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify battery specify inexistent Id </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatteryInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify battery invalid option</b>")
    command = ['battery -x', 'battery -a list -x', 'battery -a recondition -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatteryInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify battery invalid parameters</b>")
    command = ['battery test', 'battery -a test', 'battery -a recondition -b test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBatteryMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify battery missing parameters</b>")
    command = ['battery -b', 'battery -a recondition -b', 'battery -a list -b']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify battery missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyBattery(c)
    verifyBatteryList(c)
    verifyBatteryRecondition(c)
    verifyBatterySpecifyInexistentId(c)
    verifyBatteryInvalidOption(c)
    verifyBatteryInvalidParameters(c)
    verifyBatteryMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped

