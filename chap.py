# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyChap(c):
    FailFlag = False
    tolog("<b>Verify chap </b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyChapList(c):
    FailFlag = False
    tolog("<b>Verify chap -a list</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyChapAdd(c):
    FailFlag = False
    tolog("<b>Verify chap -a add</b>")
    # chap -a add -s "name=chap1, type=local, targetid=0"  Specifies target, for local chap only.

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap -a add</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyChapMod(c):
    FailFlag = False
    tolog("<b>Verify chap -a mod</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap -a mod</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyChapDel(c):
    FailFlag = False
    tolog("<b>Verify chap -a del</b>")


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap -a del</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyChapSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify chap specify inexistent Id </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyChapInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify chap invalid option</b>")
    command = ['chap -x', 'chap -a list -x', 'chap -a add -x', 'chap -a mod -x', 'chap -a del -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyChapInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify chap invalid parameters</b>")
    command = ['chap test', 'chap -a test', 'chap -a add -s test', 'chap -a mod -i test', 'chap -a del -i test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyChapMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify chap missing parameters</b>")
    command = ['chap -i', 'chap -a list -i ', 'chap -a add -s ', 'chap -a mod -i', 'chap -a del -i']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify chap missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyChap(c)
    verifyChapList(c)
    verifyChapAdd(c)
    verifyChapMod(c)
    verifyChapDel(c)
    verifyChapSpecifyInexistentId(c)
    verifyChapInvalidOption(c)
    verifyChapInvalidParameters(c)
    verifyChapMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped