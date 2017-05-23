# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyEncldiag(c):
    FailFlag = False
    tolog("<b>Verify encldiag </b>")
    # encldiag -a <action> -e <EnclosureId> -t <element type>

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag  </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyEncldiagList(c):
    FailFlag = False
    tolog("<b>Verify encldiag -a list</b>")
    # encldiag -a <action> -e <EnclosureId> -t <element type>

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEncldiagSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify encldiag specify inexistent Id </b>")
    # -e <enclosure ID> (1,16)

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEncldiagInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify encldiag invalid option</b>")
    command = ['encldiag -x', 'encldiag -a list -x', 'encldiag -a -e 1 -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEncldiagInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify encldiag invalid parameters</b>")
    command = ['encldiag test', 'encldiag -a test', 'encldiag -a list -e test', 'encldiag -a list -e 1 -t test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEncldiagMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify encldiag missing parameters</b>")
    command = ['encldiag -a ', 'encldiag -a list -e', 'encldiag -a list -e 1 -t']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify encldiag missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyEncldiag(c)
    verifyEncldiagList(c)
    verifyEncldiagSpecifyInexistentId(c)
    verifyEncldiagInvalidOption(c)
    verifyEncldiagInvalidParameters(c)
    verifyEncldiagMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped