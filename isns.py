# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyIsns(c):
    FailFlag = False
    tolog("<b>Verify isns </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIsnsList(c):
    FailFlag = False
    tolog("<b>Verify isns -a list </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIsnsMod(c):
    FailFlag = False
    tolog("<b>Verify isns -a mod</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIsnsSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify isns specify inexistent Id </b>")
    # -g <portal id>  (0,31)


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyIsnsInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify isns invalid option</b>")
    command = ['isns -x', 'isns -a list -x', 'isns -a mod -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyIsnsInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify isns invalid parameters</b>")
    command = ['isns test', 'isns -a list test', 'isns -a mod test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyIsnsMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify isns missing parameters</b>")
    command = ['isns -g', 'iscsi -a mod -t', 'iscsi -a mod -s']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify isns missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyIsns(c)
    verifyIsnsList(c)
    verifyIsnsMod(c)
    verifyIsnsSpecifyInexistentId(c)
    verifyIsnsInvalidOption(c)
    verifyIsnsInvalidParameters(c)
    verifyIsnsMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped