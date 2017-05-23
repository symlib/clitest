# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyNtp(c):
    FailFlag = False
    tolog("<b>Verify ntp </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyNtpList(c):
    FailFlag = False
    tolog("<b>Verify ntp -a list </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyNtpMod(c):
    FailFlag = False
    tolog("<b>Verify ntp -a mod</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyNtpTest(c):
    FailFlag = False
    tolog("<b>Verify ntp -a test</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp -a test </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyNtpSync(c):
    FailFlag = False
    tolog("<b>Verify ntp -a sync</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp -a sync </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyNtpInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify ntp invalid option</b>")
    command = ['ntp -x', 'ntp -a list -x', 'ntp -a mod -x', 'ntp -a test -x', 'ntp -a sync -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyNtpInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify ntp invalid parameters</b>")
    command = ['ntp test', 'ntp -a list test', 'ntp -a mod test', 'ntp -a test test', 'ntp -a sync test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyNtpMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify ntp missing parameters</b>")
    command = ['ntp -a mod -s', 'ntp -a ', 'ntp -a test -t']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify ntp missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyNtp(c)
    verifyNtpList(c)
    verifyNtpMod(c)
    verifyNtpTest(c)
    verifyNtpSync(c)
    verifyNtpInvalidOption(c)
    verifyNtpInvalidParameters(c)
    verifyNtpMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped