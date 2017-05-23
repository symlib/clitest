# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyIscsi(c):
    FailFlag = False
    tolog("<b>Verify iscsi </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIscsiList(c):
    FailFlag = False
    tolog("<b>Verify iscsi -a list</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIscsiAdd(c):
    FailFlag = False
    tolog("<b>Verify iscsi -a add</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi -add </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIscsiMod(c):
    FailFlag = False
    tolog("<b>Verify iscsi -a mod </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIscsiDel(c):
    FailFlag = False
    tolog("<b>Verify iscsi -a del </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi -a del </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyIscsiSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify iscsi specify inexistent Id </b>")
    # -i <component id>
    # -r <controller id>
    # -p <port id>

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyIscsiInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify iscsi invalid option</b>")
    command = ['iscsi -x', 'iscsi -a list -x', 'iscsi -a add -x', 'iscsi -a mod -x', 'iscsi -a del -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyIscsiInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify iscsi invalid parameters</b>")
    command = ['iscsi test', 'iscsi -a list test', 'iscsi -a add test', 'iscsi -a mod test', 'iscsi -a del test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyIscsiMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify iscsi missing parameters</b>")
    command = ['iscsi -i', 'iscsi -a list -i', 'iscsi -a add -t', 'iscsi -a mod -t', 'iscsi -a del -t']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify iscsi missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyIscsi(c)
    verifyIscsiList(c)
    verifyIscsiAdd(c)
    verifyIscsiMod(c)
    verifyIscsiDel(c)
    verifyIscsiSpecifyInexistentId(c)
    verifyIscsiInvalidOption(c)
    verifyIscsiInvalidParameters(c)
    verifyIscsiMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped