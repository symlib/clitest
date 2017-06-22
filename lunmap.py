# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def precondition(c):
    tolog("<b>add initiator</b>")
    SendCmd(c, 'initiator -a add -t iscsi -n test.lunmapadd.com')
    SendCmd(c, 'initiator -a add -t fc -n ff-cc-ff-cc-ff-cc-11-22')
    initID = []
    initIfor = SendCmd(c, 'initiator')
    initID.append(initIfor.split('Id: ')[-2].split()[0])
    initID.append(initIfor.split('Id: ')[-1].split()[0])

    tolog("<b>add volume</b>")
    volumeID = []
    poolinfo = SendCmd(c, 'pool')
    if 'No pool in the subsystem' in poolinfo:
        pdinfo = SendCmd(c, 'phydrv')
        pdID = [pdinfo.split('\r\n')[4][0]]
        SendCmd(c, 'pool -a add -p ' + pdID[0] + ' -s "name=Ptestlunmap,raid=0"')
        SendCmd(c, 'volume -a add -p 0 -s "name=Vtestlunmap,capacity=1GB"')
        volumeID = ['0']
    else:
        SendCmd(c, 'volume -a add -p 0 -s "name=Vtestlunmap1,capacity=1GB"')
        SendCmd(c, 'volume -a add -p 0 -s "name=Vtestlunmap2,capacity=1GB"')
    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[-4].split()[0]]
    return initID, volumeID

def verifyLunmapAdd(c):
    FailFlag = False
    initID, volumeID = precondition(c)

    tolog('<b>lunmap -a add -i ' + initID[1] + ' -p volume -l ' + volumeID[0] + ' -m 0</b>')
    result = SendCmd(c, 'lunmap -a add -i ' + initID[1] + ' -p volume -l ' + volumeID[0] + ' -m 0')
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Name: ff-cc-ff-cc-ff-cc-11-22' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</font>')

    tolog('<b>lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</b>')
    result = SendCmd(c, 'lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0')
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Name: test.lunmapadd.com' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a add </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmap(c):
    FailFlag = False
    tolog("<b>Verify lunmap </b>")
    result = SendCmd(c, 'lunmap')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap </font>')

    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1,len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        tolog('<b> lunmap -i ' + i + '</b>')
        result = SendCmd(c, 'lunmap -i ' + i)
        if 'Error (' in result or 'initiator: ' + i not in result:
            FailFlag = True
            tolog('<font color="red">lunmap -i ' + i + '</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapList(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a list </b>")
    result = SendCmd(c, 'lunmap -a list')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a list</font>')

    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1, len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        tolog('<b> lunmap -a list -i ' + i + '</b>')
        result = SendCmd(c, 'lunmap -a list -i ' + i)
        if 'Error (' in result or 'initiator: ' + i not in result:
            FailFlag = True
            tolog('<font color="red">lunmap -a list -i ' + i + '</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapAddlun(c):
    FailFlag = False
    tolog('<b> lunmap -a addlun </b>')
    initiatorInfo = SendCmd(c, 'initiator')
    initiatorID = [initiatorInfo.split('Id: ')[-1].split()[0]]

    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[-3].split()[0]]

    if 'No LUN mapping entry available' not in SendCmd(c, 'lunmap'):
        tolog('<b> lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023 </b>')
        result = SendCmd(c, 'lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or '1023                     ' + volumeID[0] + '                       volume' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023 </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a addlun </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDellun(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a dellun</b>")
    initiatorInfo = SendCmd(c, 'initiator')
    initiatorID = [initiatorInfo.split('Id: ')[-1].split()[0]]

    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[-3].split()[0]]

    result = SendCmd(c, 'lunmap -a dellun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0])
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Error (' in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a dellun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + '</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a dellun </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapEnable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a enable when it enable</b>")
    p1 = SendCmd(c, 'lunmap -a enable')
    if 'Error (' not in p1:
        result = SendCmd(c, 'lunmap -a enable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Enabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    tolog("<b>Verify lunmap -a enable when it disable</b>")
    p2 = SendCmd(c, 'lunmap -a disable')
    if 'Error (' not in p2:
        result = SendCmd(c, 'lunmap -a enable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Enabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDel(c):
    FailFlag = False
    result = SendCmd(c, 'lunmap')
    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1, len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        result = SendCmd(c, 'lunmap -a del -i ' + i)
        if 'Error (' in result:
            FailFlag = True
            tolog('<font color="red">lunmap -a del -i ' + i + '</font>')

    checkResult = SendCmd(c, 'lunmap')
    if 'No LUN mapping entry available' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: lunmap -a del </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a del </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDisable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a disable when it enable</b>")
    p1 = SendCmd(c, 'lunmap -a enable')
    if 'Error (' not in p1:
        result = SendCmd(c, 'lunmap -a disable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Disabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    tolog("<b>Verify lunmap -a disable when it disable</b>")
    p2 = SendCmd(c, 'lunmap -a disable')
    if 'Error (' not in p2:
        result = SendCmd(c, 'lunmap -a disable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Disabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify lunmap specify inexistent Id </b>")
    # -i <InitiatorId> (0,2047)
    # -l <Volume ID list> (0,1023)
    initiatorInfo = SendCmd(c, 'initiator')
    volumeInfo = SendCmd(c, 'volume')
    initID = initiatorInfo.split('Id: ')[-1].split()[0]
    volumeID = volumeInfo.split('\r\n')[-3].split()[0]
    if int(initID) != 2047:
        result = SendCmd(c, 'lunmap -a add -i ' + str(int(initID)+1) + ' -p volume -l ' + volumeID + ' -m 0')
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red"> lunmap -a add -i ' + str(int(initID)+1) + ' -p volume -l ' + volumeID + ' -m 0</font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    if int(volumeID) != 1023:
        result = SendCmd(c, 'lunmap -a add -i ' + initID + ' -p volume -l ' + str(int(volumeID) + 1) + ' -m 0')
        if 'Error (' not in result or 'Incorrect Parameters: Volume id' not in result:
            FailFlag = True
            tolog('<font color="red"> lunmap -a add -i ' + initID + ' -p volume -l ' + str(int(volumeID) + 1) + ' -m 0</font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify lunmap invalid option</b>")
    command = ['lunmap -x', 'lunmap -a list -x', 'lunmap -a add -x', 'lunmap -a del -x',
               'lunmap -a addlun -x', 'lunmap -a dellun -x', 'lunmap -a enable -x', 'lunmap -a disable -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify lunmap invalid parameters</b>")
    command = ['lunmap test', 'lunmap -a list test', 'lunmap -a add test', 'lunmap -a del test',
                'lunmap -a addlun test', 'lunmap -a dellun test', 'lunmap -a enable test', 'lunmap -a disable test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify lunmap missing parameters</b>")
    command = ['lunmap -i', 'lunmap -a list -i', 'lunmap -a add -i', 'lunmap -a del -i', 'lunmap -a addlun -i', 'lunmap -a dellun -i']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def bvt_verifyLunmapAdd(c):
    FailFlag = False
    initID, volumeID = precondition(c)

    tolog('<b>lunmap -a add -i ' + initID[1] + ' -p volume -l ' + volumeID[0] + ' -m 0</b>')
    result = SendCmd(c, 'lunmap -a add -i ' + initID[1] + ' -p volume -l ' + volumeID[0] + ' -m 0')
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Name: ff-cc-ff-cc-ff-cc-11-22' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</font>')

    tolog('<b>lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</b>')
    result = SendCmd(c, 'lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0')
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Name: test.lunmapadd.com' not in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a add -i ' + initID[0] + ' -p volume -l ' + volumeID[0] + ' -m 0</font>')

    return FailFlag

def bvt_verifyLunmap(c):
    FailFlag = False
    tolog("<b>Verify lunmap </b>")
    result = SendCmd(c, 'lunmap')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap </font>')

    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1,len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        tolog('<b> lunmap -i ' + i + '</b>')
        result = SendCmd(c, 'lunmap -i ' + i)
        if 'Error (' in result or 'initiator: ' + i not in result:
            FailFlag = True
            tolog('<font color="red">lunmap -i ' + i + '</font>')

    return FailFlag

def bvt_verifyLunmapList(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a list </b>")
    result = SendCmd(c, 'lunmap -a list')
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a list</font>')

    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1, len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        tolog('<b> lunmap -a list -i ' + i + '</b>')
        result = SendCmd(c, 'lunmap -a list -i ' + i)
        if 'Error (' in result or 'initiator: ' + i not in result:
            FailFlag = True
            tolog('<font color="red">lunmap -a list -i ' + i + '</font>')

    return FailFlag

def bvt_verifyLunmapAddlun(c):
    FailFlag = False
    tolog('<b> lunmap -a addlun </b>')
    initiatorInfo = SendCmd(c, 'initiator')
    initiatorID = [initiatorInfo.split('Id: ')[-1].split()[0]]

    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[-3].split()[0]]

    if 'No LUN mapping entry available' not in SendCmd(c, 'lunmap'):
        tolog('<b> lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023 </b>')
        result = SendCmd(c, 'lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or '1023                     ' + volumeID[0] + '                       volume' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a addlun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + ' -m 1023 </font>')

    return FailFlag

def bvt_verifyLunmapDellun(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a dellun</b>")
    initiatorInfo = SendCmd(c, 'initiator')
    initiatorID = [initiatorInfo.split('Id: ')[-1].split()[0]]

    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[-3].split()[0]]

    result = SendCmd(c, 'lunmap -a dellun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0])
    checkResult = SendCmd(c, 'lunmap')
    if 'Error (' in result or 'Error (' in checkResult:
        FailFlag = True
        tolog('<font color="red">Fail: lunmap -a dellun -p volume -i ' + initiatorID[0] + ' -l ' + volumeID[0] + '</font>')

    return FailFlag

def bvt_verifyLunmapEnable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a enable when it enable</b>")
    p1 = SendCmd(c, 'lunmap -a enable')
    if 'Error (' not in p1:
        result = SendCmd(c, 'lunmap -a enable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Enabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    tolog("<b>Verify lunmap -a enable when it disable</b>")
    p2 = SendCmd(c, 'lunmap -a disable')
    if 'Error (' not in p2:
        result = SendCmd(c, 'lunmap -a enable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Enabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    return FailFlag

def bvt_verifyLunmapDel(c):
    FailFlag = False
    result = SendCmd(c, 'lunmap')
    lunmapID = []
    row = result.split('initiator: ')
    for i in range(1, len(row)):
        lunmapID.append(row[i][0])

    for i in lunmapID:
        result = SendCmd(c, 'lunmap -a del -i ' + i)
        if 'Error (' in result:
            FailFlag = True
            tolog('<font color="red">lunmap -a del -i ' + i + '</font>')

    checkResult = SendCmd(c, 'lunmap')
    if 'No LUN mapping entry available' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: lunmap -a del </font>')

    return FailFlag

def bvt_verifyLunmapDisable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a disable when it enable</b>")
    p1 = SendCmd(c, 'lunmap -a enable')
    if 'Error (' not in p1:
        result = SendCmd(c, 'lunmap -a disable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Disabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    tolog("<b>Verify lunmap -a disable when it disable</b>")
    p2 = SendCmd(c, 'lunmap -a disable')
    if 'Error (' not in p2:
        result = SendCmd(c, 'lunmap -a disable')
        checkResult = SendCmd(c, 'lunmap')
        if 'Error (' in result or 'LUN mapping and masking : Disabled' not in checkResult:
            FailFlag = True
            tolog('<font color="red">Fail: lunmap -a enable </font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    return FailFlag

def bvt_verifyLunmapSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify lunmap specify inexistent Id </b>")
    # -i <InitiatorId> (0,2047)
    # -l <Volume ID list> (0,1023)
    initiatorInfo = SendCmd(c, 'initiator')
    volumeInfo = SendCmd(c, 'volume')
    initID = initiatorInfo.split('Id: ')[-1].split()[0]
    volumeID = volumeInfo.split('\r\n')[-3].split()[0]
    if int(initID) != 2047:
        result = SendCmd(c, 'lunmap -a add -i ' + str(int(initID)+1) + ' -p volume -l ' + volumeID + ' -m 0')
        if 'Error (' not in result or 'Invalid initiator index' not in result:
            FailFlag = True
            tolog('<font color="red"> lunmap -a add -i ' + str(int(initID)+1) + ' -p volume -l ' + volumeID + ' -m 0</font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    if int(volumeID) != 1023:
        result = SendCmd(c, 'lunmap -a add -i ' + initID + ' -p volume -l ' + str(int(volumeID) + 1) + ' -m 0')
        if 'Error (' not in result or 'Incorrect Parameters: Volume id' not in result:
            FailFlag = True
            tolog('<font color="red"> lunmap -a add -i ' + initID + ' -p volume -l ' + str(int(volumeID) + 1) + ' -m 0</font>')
    else:
        tolog('<font color="red"> Precondition failure </font>')

    return FailFlag

def bvt_verifyLunmapInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify lunmap invalid option</b>")
    command = ['lunmap -x', 'lunmap -a list -x', 'lunmap -a add -x', 'lunmap -a del -x',
               'lunmap -a addlun -x', 'lunmap -a dellun -x', 'lunmap -a enable -x', 'lunmap -a disable -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyLunmapInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify lunmap invalid parameters</b>")
    command = ['lunmap test', 'lunmap -a list test', 'lunmap -a add test', 'lunmap -a del test',
                'lunmap -a addlun test', 'lunmap -a dellun test', 'lunmap -a enable test', 'lunmap -a disable test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')

    return FailFlag

def bvt_verifyLunmapMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify lunmap missing parameters</b>")
    command = ['lunmap -i', 'lunmap -a list -i', 'lunmap -a add -i', 'lunmap -a del -i', 'lunmap -a addlun -i', 'lunmap -a dellun -i']
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
    verifyLunmapAdd(c)
    verifyLunmap(c)
    verifyLunmapList(c)
    verifyLunmapAddlun(c)
    verifyLunmapDellun(c)
    verifyLunmapEnable(c)
    verifyLunmapDel(c)
    verifyLunmapDisable(c)
    verifyLunmapSpecifyInexistentId(c)
    verifyLunmapInvalidOption(c)
    verifyLunmapInvalidParameters(c)
    verifyLunmapMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped