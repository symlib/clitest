# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyEnclosure(c):
    FailFlag = False
    tolog("<b>Verify enclosure </b>")
    # -e <encl id>  1
    # -i <sensor id> (1,6)
    # -f <FRU id>  1 and 2


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEnclosureList(c):
    FailFlag = False
    tolog("<b>Verify enclosure -a list </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEnclosureMod(c):
    FailFlag = False
    tolog("<b>Verify enclosure -a mod </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyEnclosureLocate(c):
    FailFlag = False
    tolog("<b>Verify enclosure -a locate </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a locate </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifEnclosureSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify enclosure specify inexistent Id </b>")
    # -e <encl id>  1
    # -i <sensor id> (1,6)
    # -f <FRU id>  1 and 2

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyEnclosureInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify enclosure invalid option</b>")
    command = ['enclosure -x', 'enclosure -a list -x', 'enclosure -a mod -x', 'enclosure -a locate -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify enclosure invalid parameters</b>")
    command = ['enclosure test', 'enclosure -a test', 'enclosure -a mod -s test', 'enclosure -a locate -t test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify enclosure missing parameters</b>")
    command = ['enclosure -a', 'enclosure -a mod -s ', 'enclosure -a list -i', 'enclosure -a locate -t']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyEnclosure(c)
    verifyEnclosureList(c)
    verifyEnclosureMod(c)
    verifyEnclosureLocate(c)
    verifEnclosureSpecifyInexistentId(c)
    verifyEnclosureInvalidOption(c)
    verifyEnclosureInvalidParameters(c)
    verifyEnclosureMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped