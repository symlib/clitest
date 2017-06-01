# coding=utf-8
# initial sample work on 2016.12.23
# this section includes verify proper cmd/parameters/options and
# some other boundary or misspelled parameters/options
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
import random
Pass = "'result': 'p'"
Fail = "'result': 'f'"
# find configured PdId in phydrv list
def findPdId(c):
    result = SendCmd(c, "phydrv")
    num = 4
    PdId = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        PdId.append(row.split()[0])
        num = num + 1
    return PdId
def verifySmart(c):
    FailFlag = False
    tolog("<b>Verify smart</b>")
    PdId = findPdId(c)
    result = SendCmd(c, "smart")
    num = 4
    smartPdId = []
    if "Error (" in result:
        tolog('\n<font color="red">Fail:smart Please check PD OpStatus</font>')
        exit()
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        smartPdId.append(row.split()[0])
        num = num + 1
    if smartPdId != PdId:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify smart</font>')
    tolog("<b>Verify smart -p </b>")
    PdId = findPdId(c)
    for m in PdId:
        result = SendCmd(c, "smart -p " + m)
        row = result.split("\r\n")
        if row[2] not in result or row[4].split()[0] != m:
            FailFlag = True
            tolog('\n<font color="red">Fail: Verify smart -p' + m + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartV(c):
    FailFlag = False
    tolog("<b>Verify smart -v</b>")
    result = SendCmd(c, "smart -v")
    if "Error (" in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify smart -v</font>')
    tolog("<b> Verify smart -v -p </b>")
    result = SendCmd(c, "smart")
    if "Error (" in result:
        tolog('\n<font color="red">Fail:smart Please check PD OpStatus</font>')
        exit()
    enablePdId = []
    disablePdId = []
    num = 4
    # get the smart enable and disable Id list
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[-1] == "Disabled":
            disablePdId.append(row.split()[0])
        if row.split()[-1] == "Enabled":
            enablePdId.append(row.split()[0])
        num = num + 1
    # When PD smart is enable, verify smart -v -p
    if len(enablePdId) != 0:
        for m in enablePdId:
            tolog('<b> smart -v -p ' + m + '</b>')
            result = SendCmd(c, "smart -v -p " + m)
            PDModel = SendCmd(c, "phydrv -v -p " + m)
            smartPDModel = result.split("\r\n")[3].split()[-1]
            if result.split("\r\n")[2] != "PdId: " + m or smartPDModel not in PDModel or "SMART Health Status: OK" not in result:
                FailFlag = True
                tolog('\n<font color="red">Fail: Verify smart -v -p ' + m + '</font>')
                tolog('\n<font color="red">Checkpoint: PdId, PDModel, SMART Health Status </font>')
    # When PD smart is disable, verify smart -v -p
    if len(disablePdId) != 0:
        for m in disablePdId:
            result = SendCmd(c, "smart -p " + m + " -v")
            PDModel = SendCmd(c, "phydrv -v -p " + m)
            smartPDModel = result.split("\r\n")[3].split()[-1]
            if result.split("\r\n")[2] != "PdId: " + m or smartPDModel not in PDModel:
                FailFlag = True
                tolog('\n<font color="red">Fail: Verify smart -v -p ' + m + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart -v </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartList(c):
    FailFlag = False
    tolog("<b>Verify smart -a list</b>")
    PdId = findPdId(c)
    result = SendCmd(c, "smart -a list")
    num = 4
    smartPdId = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        smartPdId.append(row.split()[0])
        num = num + 1
    if smartPdId != PdId:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify smart -a list</font>')
    tolog("<b>Verify smart -a list -p </b>")
    PdId = findPdId(c)
    for m in PdId:
        result = SendCmd(c, "smart -a list -p " + m)
        row = result.split("\r\n")
        if row[2] not in result or row[4].split()[0] != m:
            FailFlag = True
            tolog('\n<font color="red">Fail: Verify smart -a list -p' + m + '</font>')
    tolog('<b>Verify smart -a list -v </b>')
    result = SendCmd(c, 'smart -a list -v')
    if "Error (" in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify smart -a list -v</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartEnable(c):
    FailFlag = False
    tolog("<b> Verify smart -a enable -p pd ID </b>")
    PdId = random.choice(findPdId(c))
    for values in ['disable ', 'enable ', 'enable ']:
        result = SendCmd(c, "smart -a " + values + "-p " + PdId)
        if "Error (" in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: smart -a ' + values + '-p ' + PdId + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart -a enable -p pd ID </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartDisable(c):
    FailFlag = False
    tolog("<b> Verify smart -a disable -p pd ID </b>")
    PdId = random.choice(findPdId(c))
    for values in ['enable ', 'disable ', 'disable ']:
        result = SendCmd(c, "smart -a " + values + "-p " + PdId)
        if "Error (" in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: smart -a ' + values + '-p ' + PdId + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart -a disable -p pd ID </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartHelp(c):
    FailFlag = False
    tolog("<b> Verify smart -h </b>")
    result = SendCmd(c, "smart -h")
    if 'Error (' in result or "smart" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify smart -h </font>')
        tolog('\n<font color="red">Checkpoint: Usage, Summary, smart </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart -h </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify smart specify inexistent Id </b>")
    command1 = ['smart -p 512', 'smart -a list -p 512', 'smart -a enable -p 512', 'smart -a disable -p 512']
    command2 = ['smart -p 513', 'smart -a list -p 513', 'smart -a enable -p 513', 'smart -a disable -p 513']
    for com in command1:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "not found" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    for com in command2:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "invalid setting 513 (1,512)" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart specify inexistent Id </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify smart invalid option</b>")
    command = ['smart -x', 'smart -a list -x', 'smart -a enable -x', 'smart -a disable -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify smart invalid parameters</b>")
    command = ['smart test', 'smart -a test', 'smart -a enable -p test', 'smart -a disable -p test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifySmartMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify smart missing parameters</b>")
    command = ['smart -v -p ', 'smart -a list -p ', 'smart -p ', 'smart -a enable -p ', 'smart -a disable -p ']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify smart missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifySmart(c)
    verifySmartV(c)
    verifySmartList(c)
    verifySmartEnable(c)
    verifySmartDisable(c)
    verifySmartHelp(c)
    verifySmartSpecifyInexistentId(c)
    verifySmartInvalidOption(c)
    verifySmartInvalidParameters(c)
    verifySmartMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped