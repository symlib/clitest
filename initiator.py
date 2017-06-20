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
    result = SendCmd(c, 'initiator')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: initiator </font>')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1,len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -i ' + i)
            if 'Error (' in result or 'Id: ' + i not in result:
                FailFlag = True
                tolog('<font color="red"> initiator -i ' + i + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorList(c):
    FailFlag = False
    tolog("<b>Verify initiator -a list</b>")
    result = SendCmd(c, 'initiator -a list')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: initiator -a list </font>')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -a list -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -a list -i ' + i)
            if 'Error (' in result or 'Id: ' + i not in result:
                FailFlag = True
                tolog('<font color="red"> initiator -a list -i ' + i + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorAdd(c):
    FailFlag = False
    command = lambda type,name:'initiator -a add -t ' + type + ' -n ' + name
    tolog('<b>' + command('iscsi','a.b.com') + '</b>')
    result = SendCmd(c, command('iscsi','a.b.com'))
    checkResult = SendCmd(c, 'initiator')
    if 'Error (' in result or 'Type: iscsi' not in checkResult or 'Name: a.b.com' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: ' + command('iscsi', 'a.b.com') + '</font>')
    tolog('<b>' + command('fc', 'aa-bb-cc-dd-ee-ff-11-22') + '</b>')
    result = SendCmd(c, command('fc', 'aa-bb-cc-dd-ee-ff-11-22'))
    checkResult = SendCmd(c, 'initiator')
    if 'Error (' in result or 'Type: fc' not in checkResult or 'Name: aa-bb-cc-dd-ee-ff-11-22' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: ' + command('iscsi', 'a.b.com') + '</font>')
    tolog('<b>' + command('fc', 'aa-bb-cc-dd-ee-ff-11-22') + '</b>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator -a add </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorDel(c):
    FailFlag = False
    result = SendCmd(c, 'initiator')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -a del -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -a del -i ' + i)
            if 'Error (' in result:
                FailFlag = True
                tolog('<font color="red"> initiator -a del -i ' + i + '</font>')
        checkResult = SendCmd(c, 'initiator')
        if 'Error (' in checkResult or 'No initiator entry available' not in checkResult:
            FailFlag = True
            tolog('\n<font color="red">Fail: initiator -a del </font>')
    else:
        FailFlag = True
        tolog('\n<font color="red">Fail: There is no initiator can be deleted </font>')
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
    result = SendCmd(c, 'initiator')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
    command = lambda action,i:'initiator -a ' + action + ' -i ' + i
    if len(ii) != 0:
        tolog('<b>' + command('del', str(int(ii[-1])+1)) + '</b>')
        result = SendCmd(c, command('del', str(int(ii[-1])+1)))
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('del', str(int(ii[-1]) + 1)) + '</font>')
        tolog('<b>' + command('list', str(int(ii[-1])+1)) + '</b>')
        result = SendCmd(c, command('list', str(int(ii[-1])+1)))
        if 'No initiator entry available' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('list', str(int(ii[-1])+1)) + '</font>')
    else:
        tolog('<b>' + command('del', '1') + '</b>')
        result = SendCmd(c, command('del', '1'))
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('del', '1') + '</font>')
        tolog('<b>' + command('list', '1') + '</b>')
        result = SendCmd(c, command('list', '1'))
        if 'No initiator entry available' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('list', '1') + '</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify initiator specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyInitiatorInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify initiator invalid option</b>")
    command = ['initiator -x',
               'initiator -a list -x',
               'initiator -a add -x',
               'initiator -a del -x',
               ]
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
    command = ['initiator test',
               'initiator -a list -i 2048',
               'initiator -a add test',
               'initiator -a del -i 2048',
               ]
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


def bvt_verifyInitiator(c):
    FailFlag = False
    tolog("<b>Verify initiator </b>")
    result = SendCmd(c, 'initiator')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: initiator </font>')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1,len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -i ' + i)
            if 'Error (' in result or 'Id: ' + i not in result:
                FailFlag = True
                tolog('<font color="red"> initiator -i ' + i + '</font>')

    return FailFlag

def bvt_verifyInitiatorList(c):
    FailFlag = False
    tolog("<b>Verify initiator -a list</b>")
    result = SendCmd(c, 'initiator -a list')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: initiator -a list </font>')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -a list -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -a list -i ' + i)
            if 'Error (' in result or 'Id: ' + i not in result:
                FailFlag = True
                tolog('<font color="red"> initiator -a list -i ' + i + '</font>')

    return FailFlag

def bvt_verifyInitiatorAdd(c):
    FailFlag = False
    command = lambda type,name:'initiator -a add -t ' + type + ' -n ' + name
    tolog('<b>' + command('iscsi','a.b.com') + '</b>')
    result = SendCmd(c, command('iscsi','a.b.com'))
    checkResult = SendCmd(c, 'initiator')
    if 'Error (' in result or 'Type: iscsi' not in checkResult or 'Name: a.b.com' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: ' + command('iscsi', 'a.b.com') + '</font>')
    tolog('<b>' + command('fc', 'aa-bb-cc-dd-ee-ff-11-22') + '</b>')
    result = SendCmd(c, command('fc', 'aa-bb-cc-dd-ee-ff-11-22'))
    checkResult = SendCmd(c, 'initiator')
    if 'Error (' in result or 'Type: fc' not in checkResult or 'Name: aa-bb-cc-dd-ee-ff-11-22' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: ' + command('iscsi', 'a.b.com') + '</font>')
    tolog('<b>' + command('fc', 'aa-bb-cc-dd-ee-ff-11-22') + '</b>')

    return FailFlag

def bvt_verifyInitiatorDel(c):
    FailFlag = False
    result = SendCmd(c, 'initiator')
    ii = []
    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
        for i in ii:
            tolog('<b> initiator -a del -i ' + i + '</b>')
            result = SendCmd(c, 'initiator -a del -i ' + i)
            if 'Error (' in result:
                FailFlag = True
                tolog('<font color="red"> initiator -a del -i ' + i + '</font>')
        checkResult = SendCmd(c, 'initiator')
        if 'Error (' in checkResult or 'No initiator entry available' not in checkResult:
            FailFlag = True
            tolog('\n<font color="red">Fail: initiator -a del </font>')
    else:
        FailFlag = True
        tolog('\n<font color="red">Fail: There is no initiator can be deleted </font>')

    return FailFlag

def bvt_verifyInitiatorSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify initiator specify inexistent Id </b>")
    # -i <Index> (0,2047)
    result = SendCmd(c, 'initiator')
    ii = []

    if 'No initiator entry available' not in result:
        row = result.split('Id: ')
        for l in range(1, len(row)):
            ii.append(row[l].split()[0])
    command = lambda action,i:'initiator -a ' + action + ' -i ' + i

    if len(ii) != 0:
        tolog('<b>' + command('del', str(int(ii[-1])+1)) + '</b>')
        result = SendCmd(c, command('del', str(int(ii[-1])+1)))
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('del', str(int(ii[-1]) + 1)) + '</font>')
        tolog('<b>' + command('list', str(int(ii[-1])+1)) + '</b>')
        result = SendCmd(c, command('list', str(int(ii[-1])+1)))
        if 'No initiator entry available' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('list', str(int(ii[-1])+1)) + '</font>')
    else:
        tolog('<b>' + command('del', '1') + '</b>')
        result = SendCmd(c, command('del', '1'))
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('del', '1') + '</font>')
        tolog('<b>' + command('list', '1') + '</b>')
        result = SendCmd(c, command('list', '1'))
        if 'No initiator entry available' not in result:
            FailFlag = True
            tolog('<font color="red">' + command('list', '1') + '</font>')

    return FailFlag

def bvt_verifyInitiatorInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify initiator invalid option</b>")
    command = ['initiator -x',
               'initiator -a list -x',
               'initiator -a add -x',
               'initiator -a del -x',
               ]
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyInitiatorInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify initiator invalid parameters</b>")
    command = ['initiator test',
               'initiator -a list -i 2048',
               'initiator -a add test',
               'initiator -a del -i 2048',
               ]
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyInitiatorMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify initiator missing parameters</b>")
    command = ['initiator -i', 'initiator -a list -i', 'initiator -a add -i', 'initiator -a del -i']
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