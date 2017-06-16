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
    command = ['enclosure', 'enclosure -e 1', 'enclosure -v']
    listCheckPoint = ['SBB-SAS-12G-2U-12Bay', '> 2000 RPM']
    for com in command[0:2]:
        tolog('<b>Verify ' + com + ' </b>')
        result = SendCmd(c, com)
        if 'Error (' in result or listCheckPoint[0] not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + '</font>')
    result = SendCmd(c, command[2])
    if listCheckPoint[0] not in result or listCheckPoint[1] not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: ' + command[2] + '</font>')

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureList(c):
    FailFlag = False
    command = ['enclosure -a list', 'enclosure -a list -e 1', 'enclosure -a list -v']
    listCheckPoint = ['SBB-SAS-12G-2U-12Bay', '> 2000 RPM']
    for com in command[0:2]:
        tolog('<b>Verify ' + com + ' </b>')
        result = SendCmd(c, com)
        if 'Error (' in result or listCheckPoint[0] not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + '</font>')
    result = SendCmd(c, command[2])
    if listCheckPoint[0] not in result or listCheckPoint[1] not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: ' + command[2] + '</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a list </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureMod(c):
    FailFlag = False
    tolog("<b>Verify enclosure -a mod </b>")
    TW = [47, 51]
    TC = [57, 61]
    for index in range(0, 1):
        tolog('<b> enclosure -a mod -s "tempwarning=' + str(TW[index]) + ',tempcritical=' + str(TC[index]) + '"</b>')
        result = SendCmd(c, 'enclosure -a mod -s "tempwarning=' + str(TW[index]) + ',tempcritical=' + str(TC[index]) + '"')
        checkResult = SendCmd(c, 'enclosure -v')
        if "Error (" in result or str(TW[index]) + 'C' not in checkResult or str(TC[index]) + 'C' not in checkResult:
            FailFlag = True
            tolog('\n<font color="red">Fail: enclosure -a mod -s "tempwarning=' + str(TW[index]) + ',tempcritical=' + str(TC[index]) + '"</font>')

    def verifyCtrlTempSetting(c, option1, option2, i):
        FailFlag = False
        tolog('<b> enclosure -a mod -s "ctrltempwarning=' + option1 + ',ctrltempcritical=' + option2 + '" -i ' + i + '"</b>')
        result = SendCmd(c, 'enclosure -a mod -s "ctrltempwarning=' + option1 + ',ctrltempcritical=' + option2 + '" -i '+ i)
        checkResult = SendCmd(c, 'enclosure -v')
        if "Error (" in result or option1 + 'C' not in checkResult or option2 + 'C' not in checkResult:
            FailFlag = True
            tolog('\n<font color="red">Fail: enclosure -a mod -s "ctrltempwarning=' + option1 + ',ctrltempcritical=' + option2 + '" -i ' + i + '"</font>')
        return FailFlag

    if verifyCtrlTempSetting(c, '62', '69', '1'):
        FailFlag = True
    if verifyCtrlTempSetting(c, '63', '71', '4'):
        FailFlag = True
    if verifyCtrlTempSetting(c, '67', '74', '2'):
        FailFlag = True
    if verifyCtrlTempSetting(c, '69', '76', '5'):
        FailFlag = True
    if verifyCtrlTempSetting(c, '72', '82', '3'):
        FailFlag = True
    if verifyCtrlTempSetting(c, '77', '87', '6'):
        FailFlag = True
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a mod </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureLocate(c):
    FailFlag = False
    def locateSetting(c, t, f):
        tolog('<b>Verify enclosure -a locate -t ' + t + ' -f ' + f + ' </b>')
        result = SendCmd(c, 'enclosure -a locate -t ' + t + ' -f ' + f)
        if "Error (" in result:
            FailFlag = True
            tolog('\n<font color="red"> enclosure -a locate -t ' + t + ' -f ' + f + '</font>')
            return FailFlag
    locateSetting(c, 'ctrl', '1')
    locateSetting(c, 'cooling', '1')
    locateSetting(c, 'psu', '1')
    locateSetting(c, 'ctrl', '2')
    locateSetting(c, 'cooling', '2')
    locateSetting(c, 'psu', '2')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -a locate </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyEnclosureHelp(c):
    FailFlag = False
    tolog("<b>Verify enclosure -h </b>")
    result = SendCmd(c, 'enclosure -h')
    if 'Error (' in result or 'enclosure' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: enclosure -h </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify enclosure -h </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifEnclosureSpecifyInexistentId(c):
    FailFlag = False
    tolog("<b> Verify enclosure specify inexistent Id </b>")
    # -e <encl id>  (1,16)
    # -i <sensor id> (1,6)
    # -f <FRU id>  1 and 2
    command = ['enclosure -e 0',
               'enclosure -a mod -s "ctrltempwarning=70, ctrltempcritical=75" -i 7',
               'enclosure -a mod -s "ctrltempwarning=70, ctrltempcritical=75" -i 0',
               'enclosure -a locate -t ctrl -f 0'
               'enclosure -a locate -t ctrl -f 3'
               ]
    for com in command:
        tolog('<b>' + com + '</b>')
        result = SendCmd(c, com)
        if 'Error (' not in result or 'Invalid setting parameters' not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + '</font>')

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
    command = ['enclosure test',
               'enclosure -a test',
               'enclosure -a mod -s test',
               'enclosure -a locate -t test',
               'enclosure -a mod -s "tempwarning=46"',
               'enclosure -a mod -s "tempcritical=56"',
               'enclosure -a mod -i 1 -s "ctrltempwarning=60"',
               'enclosure -a mod -i 4 -s "ctrltempcritical=67"',
               'enclosure -a mod -i 2 -s "ctrltempwarning=65"',
               'enclosure -a mod -i 5 -s "ctrltempcritical=72"',
               'enclosure -a mod -i 3 -s "ctrltempwarning=70"',
               'enclosure -a mod -i 6 -s "ctrltempcritical=80"',
               ]
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
    # verifyEnclosure(c)
    # verifyEnclosureList(c)
    verifyEnclosureMod(c)
    # verifyEnclosureLocate(c)
    # verifyEnclosureHelp(c)
    # verifEnclosureSpecifyInexistentId(c)
    # verifyEnclosureInvalidOption(c)
    # verifyEnclosureInvalidParameters(c)
    # verifyEnclosureMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped