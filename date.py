# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyDate(c):
    FailFlag = False
    tolog("<b>Verify date </b>")
    result = SendCmd(c, 'date')
    if 'Error (' in result or 'SystemDate:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateList(c):
    FailFlag = False
    tolog("<b>Verify date -a list </b>")
    result = SendCmd(c, 'date -a list')
    if 'Error (' in result or 'SystemDate:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a list </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateMod(c):
    FailFlag = False
    tolog("<b>Verify date -a mod </b>")
    # yyyy/mm/dd where month's range is 1-12 and day's range is 1-31.
    # hh:mm:ss where hour's range is 0-23, minute's and seconds'range are 0-59
    SendCmd(c, 'date -a mod -d 2018/01/01')
    c, ssh = ssh_conn()
    result = SendCmd(c, 'date')
    if '2018-01-01' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a mod -d 2018/01/01 </font>')

    SendCmd(c, 'date -a mod -t 08:08:08')
    c, ssh = ssh_conn()
    result = SendCmd(c, 'date')
    if '08:08:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a mod -t 08:08:08 </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateHelp(c):
    FailFlag = False
    tolog("<b>Verify date -h </b>")
    result = SendCmd(c, 'date -h')
    if 'Error (' in result or 'date' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -h </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date -h </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify date invalid option</b>")
    command = ['date -x', 'date -a list -x', 'date -a mod -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify date invalid parameters</b>")
    command = ['date test', 'date -a test', 'date -a mod -d 2017/13/30', 'date -a mod -d 2017/05/33',
               'date -a mod -t 24:00:00', 'date -a mod -t 00:61:00', 'date -a mod -t 00:00:61']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyDateMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify date missing parameters</b>")
    command = ['date -a mod -d', 'date -a mod -t']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify date missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def bvt_verifyDate(c):
    FailFlag = False
    tolog("<b>Verify date </b>")
    result = SendCmd(c, 'date')
    if 'Error (' in result or 'SystemDate:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date </font>')

    return FailFlag

def bvt_verifyDateList(c):
    FailFlag = False
    tolog("<b>Verify date -a list </b>")
    result = SendCmd(c, 'date -a list')
    if 'Error (' in result or 'SystemDate:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a list </font>')

    return FailFlag

def bvt_verifyDateMod(c):
    FailFlag = False
    tolog("<b>Verify date -a mod </b>")
    # yyyy/mm/dd where month's range is 1-12 and day's range is 1-31.
    # hh:mm:ss where hour's range is 0-23, minute's and seconds'range are 0-59
    SendCmd(c, 'date -a mod -d 2018/01/01')
    c, ssh = ssh_conn()
    result = SendCmd(c, 'date')
    if '2018-01-01' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a mod -d 2018/01/01 </font>')

    SendCmd(c, 'date -a mod -t 08:08:08')
    c, ssh = ssh_conn()
    result = SendCmd(c, 'date')
    if '08:08:' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -a mod -t 08:08:08 </font>')

    return FailFlag

def bvt_verifyDateHelp(c):
    FailFlag = False
    tolog("<b>Verify date -h </b>")
    result = SendCmd(c, 'date -h')
    if 'Error (' in result or 'date' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: date -h </font>')

    return FailFlag

def bvt_verifyDateInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify date invalid option</b>")
    command = ['date -x', 'date -a list -x', 'date -a mod -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyDateInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify date invalid parameters</b>")
    command = ['date test', 'date -a test', 'date -a mod -d 2017/13/30', 'date -a mod -d 2017/05/33',
               'date -a mod -t 24:00:00', 'date -a mod -t 00:61:00', 'date -a mod -t 00:00:61']

    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyDateMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify date missing parameters</b>")
    command = ['date -a mod -d', 'date -a mod -t']

    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag


if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyDate(c)
    verifyDateList(c)
    verifyDateMod(c)
    verifyDateHelp(c)
    verifyDateInvalidOption(c)
    verifyDateInvalidParameters(c)
    verifyDateMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped