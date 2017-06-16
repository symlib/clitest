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
    SendCmd(c, 'initiator -a add -t fc -n te-st-lu-nm-ap-ad-d0-22')
    initID = []
    initIfor = SendCmd(c, 'initiator')
    initID.append(initIfor.split('Id: ')[-4][0])
    initID.append(initIfor.split('Id: ')[-3][0])

    tolog("<b>add volume</b>")
    volumeID = []
    poolinfo = SendCmd(c, 'pool')
    if 'No pool in the subsystem' in poolinfo:
        pdinfo = SendCmd(c, 'phydrv')
        pdID = [pdinfo.split('\r\n')[4][0]]
        SendCmd(c, 'pool -a add -p ' + pdID[0] + ' -s "name=Ptestlunmap,raid=0"')
        SendCmd(c, 'volume -a add -p 0 -s "name=Vtestlunmap,capacity=1GB"')
        volumeID = ['0']
    volumeInfo = SendCmd(c, 'volume')
    volumeID = [volumeInfo.split('\r\n')[4][0]]
    return initID, volumeID

def verifyLunmap(c):
    FailFlag = False
    tolog("<b>Verify lunmap </b>")



    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapList(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a list </b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapAdd(c):
    FailFlag = False
    initID, volumeID = precondition(c)

    result = SendCmd(c, 'lunmap -a add -i ' + initID[0] + ' -p volume -l 0 -m 0')
    checkResult = SendCmd(c, 'lunmap')


    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a add </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDel(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a del</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a del </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapAddvol(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a addvol</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a addvol </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDelvol(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a delvol</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a delvol </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapEnable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a enable</b>")

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify lunmap -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyLunmapDisable(c):
    FailFlag = False
    tolog("<b>Verify lunmap -a disable</b>")

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
               'lunmap -a addvol -x', 'lunmap -a delvol -x', 'lunmap -a enable -x', 'lunmap -a disable -x']
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
                'lunmap -a addvol test', 'lunmap -a delvol test', 'lunmap -a enable test', 'lunmap -a disable test']
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
    command = ['lunmap -i', 'lunmap -a list -i', 'lunmap -a add -i', 'lunmap -a del -i', 'lunmap -a addvol -i', 'lunmap -a delvol -i']
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

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    precondition(c)
    # verifyLunmap(c)
    # verifyLunmapList(c)
    # verifyLunmapAdd(c)
    # verifyLunmapDel(c)
    # verifyLunmapAddvol(c)
    # verifyLunmapDelvol(c)
    # verifyLunmapEnable(c)
    # verifyLunmapDisable(c)
    # verifyLunmapSpecifyInexistentId(c)
    # verifyLunmapInvalidOption(c)
    # verifyLunmapInvalidParameters(c)
    # verifyLunmapMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped