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
def verifyBuzzerEnableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

def verifyBuzzerEnableAndSoundingTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a on")
    if "Error (" not in result or "Buzzer is disabled" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "Yes" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInfo(c):
    FailFlag = False
    tolog('<b>Verify buzz</b>')
    result = SendCmd(c, 'buzz')
    if "Error (" in result or "Enabled" not in result or "Status" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerHelp(c):
    FailFlag = False
    tolog('<b>Verify buzz -h </b>')
    result = SendCmd(c, 'buzz -h')
    if "Error (" in result or "buzz" not in result or "Usage" not in result or "Summary" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -h</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -h</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInvalidParameters(c):
    FailFlag = False
    tolog('<b>Verify buzzer abc</b>')
    result = SendCmd(c, 'buzz abc')
    if "Error (" not in result or "parameters" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz abc</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz abc </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInvalidOption(c):
    FailFlag = False
    tolog('<b>Verify buzzer -x</b>')
    result = SendCmd(c, 'buzz -x')
    if "Error (" not in result or "Invalid option" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -x</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -x </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def BVTverifyBuzzerEnableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSoundingTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')

    return FailFlag


def BVTverifyBuzzerDisableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a on")
    if "Error (" not in result or "Buzzer is disabled" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSoundingTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')

    return FailFlag

def BVTverifyBuzzerDisableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')

    return FailFlag


def BVTverifyBuzzerDisableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "Yes" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSoundingEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSoundingDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')

    return FailFlag


def BVTverifyBuzzerEnableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')

    return FailFlag


def BVTverifyBuzzerDisableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable </font>')

    return FailFlag


def BVTverifyBuzzerInfo(c):
    FailFlag = False
    tolog('<b>Verify buzz</b>')
    result = SendCmd(c, 'buzz')
    if "Error (" in result or "Enabled" not in result or "Status" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz</font>')

    return FailFlag


def BVTverifyBuzzerHelp(c):
    FailFlag = False
    tolog('<b>Verify buzz -h </b>')
    result = SendCmd(c, 'buzz -h')
    if "Error (" in result or "buzz" not in result or "Usage" not in result or "Summary" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -h</font>')

    return FailFlag


def BVTverifyBuzzerInvalidParameters(c):
    FailFlag = False
    tolog('<b>Verify buzzer abc</b>')
    result = SendCmd(c, 'buzz abc')
    if "Error (" not in result or "parameters" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz abc</font>')

    return FailFlag


def BVTverifyBuzzerInvalidOption(c):
    FailFlag = False
    tolog('<b>Verify buzzer -x</b>')
    result = SendCmd(c, 'buzz -x')
    if "Error (" not in result or "Invalid option" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -x</font>')


    return FailFlag

    return FailFlag

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
def verifyBuzzerEnableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a on")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentTurnOn(c):
    FailFlag = False
    tolog('<b>Verify buzz -a on</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a on")
    if "Error (" not in result or "Buzzer is disabled" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a on</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a on </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if 'Error' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentTurnOff(c):
    FailFlag = False
    tolog('<b>Verify buzz -a off</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a off")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a off</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a off </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "Yes" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingEnable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a enable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a enable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Sounding' not in checkResult or 'Yes' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a enable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a enable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSoundingDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a on")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerEnableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a enable"), SendCmd(c, "buzz -a off")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if 'Error (' in result or 'Silent' not in checkResult or 'No' not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerDisableAndSilentDisable(c):
    FailFlag = False
    tolog('<b>Verify buzz -a disable</b>')
    SendCmd(c, "buzz -a disable")
    result = SendCmd(c, "buzz -a disable")
    checkResult = SendCmd(c, "buzz")
    if "Error (" in result or "No" not in checkResult or "Silent" not in checkResult:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -a disable </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -a disable </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInfo(c):
    FailFlag = False
    tolog('<b>Verify buzz</b>')
    result = SendCmd(c, 'buzz')
    if "Error (" in result or "Enabled" not in result or "Status" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerHelp(c):
    FailFlag = False
    tolog('<b>Verify buzz -h </b>')
    result = SendCmd(c, 'buzz -h')
    if "Error (" in result or "buzz" not in result or "Usage" not in result or "Summary" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -h</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -h</font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInvalidParameters(c):
    FailFlag = False
    tolog('<b>Verify buzzer abc</b>')
    result = SendCmd(c, 'buzz abc')
    if "Error (" not in result or "parameters" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz abc</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz abc </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyBuzzerInvalidOption(c):
    FailFlag = False
    tolog('<b>Verify buzzer -x</b>')
    result = SendCmd(c, 'buzz -x')
    if "Error (" not in result or "Invalid option" not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: buzz -x</font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify buzz -x </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyBuzzerDisableAndSilentTurnOn(c)
    verifyBuzzerEnableAndSilentTurnOn(c)
    verifyBuzzerEnableAndSoundingTurnOn(c)
    verifyBuzzerDisableAndSilentTurnOff(c)
    verifyBuzzerEnableAndSilentTurnOff(c)
    verifyBuzzerEnableAndSoundingTurnOff(c)
    verifyBuzzerDisableAndSilentEnable(c)
    verifyBuzzerEnableAndSilentEnable(c)
    verifyBuzzerEnableAndSoundingEnable(c)
    verifyBuzzerEnableAndSoundingDisable(c)
    verifyBuzzerEnableAndSilentDisable(c)
    verifyBuzzerDisableAndSilentDisable(c)
    verifyBuzzerInfo(c)
    verifyBuzzerHelp(c)
    verifyBuzzerInvalidParameters(c)
    verifyBuzzerInvalidOption(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped

