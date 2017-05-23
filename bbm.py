# coding=utf-8
# initial sample work on 2016.12.23
# this section includes verify proper cmd/parameters/options and
# some other boundary or misspelled parameters/options
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
from pool import getavailpd
from pool import bvtsparedelete
from pool import poolcleanup
from pool import poolcreateandlist
from pool import sparedrvcreate

import random
Pass = "'result': 'p'"
Fail = "'result': 'f'"
def findPdId(c, l, attr):
    result = SendCmd(c, 'phydrv')
    num = 4
    PdId = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[l][:-1] == attr:
            PdId.append(row.split()[0])
        num = num + 1
    return PdId

def verifyBBM(c):
    FailFlag = False
    tolog("<b>Verify bbm</b>")
    PDCS= ['WriteCach', 'ReadCach', 'S', 'Dedicate', 'Pool']
    UnCSPd = findPdId(c, -1, 'Unconfigure')
    if len(findPdId(c, -1, PDCS[0])) == 0:
        SendCmd(c, 'wcache -a add -p ' + UnCSPd[0] + ',' + UnCSPd[1])
    if len(findPdId(c, -1, PDCS[1])) == 0:
        SendCmd(c, 'rcache -a add -p ' + UnCSPd[2])
    if len(findPdId(c, -1, PDCS[2])) == 0:
        SendCmd(c, 'spare -a add -p ' + UnCSPd[3] + ' -t g -r y')
    if len(findPdId(c, -1, PDCS[3])) == 0:
        SendCmd(c, 'spare -a add -p ' + UnCSPd[4] + ' -t d -r y')
    if len(findPdId(c, -1, PDCS[4])) == 0:
        SendCmd(c, 'pool -a add -s "name=testBBM,raid=0" ' + '-p ' + UnCSPd[5])
    result = SendCmd(c, 'bbm')
    for cs in PDCS:
        for x in findPdId(c, -1, cs):
            if 'Physical Drive Id: ' + x not in result:
                FailFlag = True
                tolog('\n<font color="red">Fail: bbm</font>')


    tolog("<b>Verify bbm -p PD's ID that the configstatus is configured</b>")
    # pdid = []
    # for m in pdid:
    #     result = SendCmd(c, "bbm -p " + m)
    #     if "Error" in result or "Drive Id: " +m not in result:
    #         FailFlag = True
    #         tolog('\n<font color="red">Fail: bbm -p ' + m + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBBMList(c):
    FailFlag = False
    tolog("<b>Verify bbm -a list </b>")
    # find configured PdId in bbm list and verify bbm
    pdid = PDInfo(c, 0)
    result = SendCmd(c, "bbm -a list")
    num = 2
    bbmpdid = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        print result.split("\r\n")[num]
        if "Drive Id:" in result.split("\r\n")[num]:
            bbmpdid.append(result.split("\r\n")[num].split()[-1])
        num = num + 1
    if pdid != bbmpdid:
        FailFlag = True
        tolog('\n<font color="red">Fail: Verify bbm -a list</font>')
    tolog("<b>Verify bbm -p PD's ID that the configstatus is configured</b>")
    pdid = findPdId(c)
    for m in pdid:
        result = SendCmd(c, "bbm -a list -p " + m)
        if "Error" in result or "Drive Id: " + m not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: bbm -a list -p ' + m + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm -a list</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMClear(c):
    FailFlag = False
    tolog("<b>Verify bbm -a clear -p pd ID (configured SATA physical drive)</b>")
    result = SendCmd(c, "phydrv")
    num = 4
    pdid = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[2] != "SAST":
            FailFlag = True
            tolog('\n<font color="red">Fail: there is no SAST type PD</font>')
            break
        if row.split()[2] == "SAST" and row.split()[-1] != "Unconfigured":
            pdid.append(row.split()[0])
        num = num + 1
    if len(pdid) != 0:
        for m in pdid:
            result = SendCmd(c, "bbm -a clear " + m)
            if "Error" in result:
                FailFlag = True
                tolog('\n<font color="red">Fail: Verify bbm -a clear ' + m + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Verify bbm -a clear -p pd ID (configured SATA physical drive)</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMHelp(c):
    FailFlag = False
    tolog("<b>Verify bbm -h</b>")
    result = SendCmd(c, "bbm -h")
    if "Usage" not in result or "Summary" not in result or "bbm" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: bbm -h </font>')
    if FailFlag:
        tolog('\n<font color="red">Verify bbm -h </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMClearFailedTest(c):
    FailFlag = False
    tolog("<b>Verify bbm -a clear -p pd id (unconfigured SATA physical drive)</b>")
    result = SendCmd(c, "phydrv")
    num = 4
    pdid = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[2] != "SAST":
            FailFlag = True
            tolog('\n<font color="red"> Fail: there is no SAST type PD </font>')
            break
        if row.split()[2] == "SAST" and row.split()[-1] == "Unconfigured":
            pdid.append(row.split()[0])
        num = num + 1
    if len(pdid) != 0:
        for m in pdid:
            result = SendCmd(c, "bbm -a clear " + m)
            if "Error" in result:
                FailFlag = True
                tolog('\n<font color="red">Fail: Verify bbm -a clear ' + m + '</font>')

    tolog("<b> Verify bbm -a clear -p pd id(configured not SATA physical drive)</b>")
    result = SendCmd(c, "phydrv")
    num = 4
    pdid = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[2] != "SAST" and row.split()[-1] != "Unconfigured":
            pdid.append(row.split()[0])
        num = num + 1
    Rpdid = random.choice(pdid)
    result = SendCmd(c, "bbm -a clear -p " + Rpdid)
    if "Error" not in result:
        FailFlag =True
        tolog('\n<font color="red">Fail: bbm -a clear -p ' + Rpdid + '</font>')

    tolog("<b>Verify bbm -a clear -p pd id(Unconfigured not SATA physical drive)</b>")
    result = SendCmd(c, "phydrv")
    num = 4
    pdid = []
    while result.split("\r\n")[num] != 'administrator@cli> ':
        row = result.split("\r\n")[num]
        if row.split()[2] != "SAST" and row.split()[-1] == "Unconfigured":
            pdid.append(row.split()[0])
        num = num + 1
    Rpdid = random.choice(pdid)
    result = SendCmd(c, "bbm -a clear -p " + Rpdid)
    if "Error" not in result:
        FailFlag =True
        tolog('\n<font color="red">Fail: bbm -a clear -p ' + Rpdid + '</font>')

    tolog("<b> Verify bbm -a clear -p pd's ID </b>")
    result = SendCmd(c, "bbm -a clear -p 1")
    if "Error" not in result:
        FailFlag = True
        tolog('\n<font color="red"> Fail: bbm -a clear -p pd ID </font>')

    if FailFlag:
        tolog('\n<font color="red">Verify bbm -a clear failed test</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b>Verify bbm specify inexistent CtrlId</b>")
    command = ['bbm -p 256', 'bbm -a list -p 256', 'bbm -a clear -p 256']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "nvalid physical drive id" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm specify inexistent CtrlId </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify bbm invalid option</b>")
    command = ['bbm -x', 'bbm -a list -x', 'bbm -a clear -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify ctrl invalid parameters</b>")
    command = ['bbm test', 'bbm -a test', 'bbm -a clear -p test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBBMMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify bbm missing parameters</b>")
    command = ['bbm -p', 'bbm -a list -p', 'bbm -a clear -p']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify bbm missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyBBM(c)
    # verifyBBMList(c)
    # verifyBBMClear(c)
    # verifyBBMHelp(c)
    # verifyBBMClearFailedTest(c)
    # verifyBBMSpecifyInexistentId(c)
    # verifyBBMInvalidOption(c)
    # verifyBBMInvalidParameters(c)
    # verifyBBMMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped