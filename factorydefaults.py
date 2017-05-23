# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def verifyFactorydefaultsRestore(c):
    FailFlag = False
    tolog("<b>Verify factorydefaults -a restore </b>")
    # factorydefaults -a <action> -t <type>
    # action = restore
    type=['all', 'allfw', 'bga', 'ctrl', 'encl', 'fc', 'iscsi', 'netmgmt', 'phydrv', 'sas', 'scsi', 'subsys',
           'allsw', 'bgasched', 'service', 'webserver', 'snmp', 'telnet', 'ssh', 'email', 'netsend', 'cim',
          'ntp', 'user', 'ups', 'ldap', 'syslog']

    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)


def verifyFactorydefaultsInvalidOption(c):
    FailFlag = False
    tolog("<b>Verify factorydefaults invalid option</b>")
    command = ['factorydefaults -x', 'factorydefaults -a restore -x']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid option" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults invalid option </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyFactorydefaultsInvalidParameters(c):
    FailFlag = False
    tolog("<b>Verify factorydefaults invalid parameters</b>")
    command = ['factorydefaults test', 'factorydefaults -a restore test']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Invalid setting parameters" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults invalid parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyFactorydefaultsMissingParameters(c):
    FailFlag = False
    tolog("<b>Verify factorydefaults missing parameters</b>")
    command = ['factorydefaults -a', 'factorydefaults -a restore -t ']
    for com in command:
        tolog('<b> Verify ' + com + '</b>')
        result = SendCmd(c, com)
        if "Error (" not in result or "Missing parameter" not in result:
            FailFlag = True
            tolog('\n<font color="red">Fail: ' + com + ' </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults missing parameters </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    verifyFactorydefaultsRestore(c)
    verifyFactorydefaultsInvalidOption(c)
    verifyFactorydefaultsInvalidParameters(c)
    verifyFactorydefaultsMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped