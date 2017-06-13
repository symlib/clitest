# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from to_log import *
from ssh_connect import ssh_conn
Pass = "'result': 'p'"
Fail = "'result': 'f'"
def factorydefaultsRestoreSetting(c, type):
    FailFlag = False
    tolog('<b> factorydefaults -a restore -t ' + type + '</b>')
    result = SendCmd(c, 'factorydefaults -a restore -t ' + type)
    if 'Error (' in result:
        FailFlag = True
        tolog('<font color="red"> factorydefaults -a restore -t ' + type + '</font>')
    return FailFlag

def factorydefaultsBga(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'bga'):
        FailFlag =True
    checkResult = SendCmd(c, 'bga')
    if 'RebuildRate: High' not in checkResult or 'RCRate: Medium' not in checkResult:
        FailFlag = True
        tolog('<font color="red"> Fail: factorydefaults -a restore -t bga </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t bga </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsCtrl(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'ctrl'):
        FailFlag =True
    checkResult = SendCmd(c, 'ctrl -v')
    checkpoint = ['Alias:',
                  'PowerSavingIdleTime: Never',
                  'PowerSavingStandbyTime: Never',
                  'PowerSavingStoppedTime: Never',
                  ]
    for cp in checkpoint:
        if cp not in checkResult:
            FailFlag = True
            tolog('<font color="red"> Fail: factorydefaults -a restore -t ctrl </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t ctrl </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsEncl(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'encl'):
        FailFlag =True
    checkResult = SendCmd(c, 'enclosure -v')
    checkpoint = ['Enclosure                 51C/123F                 61C/141F',
                  'Controller 1 Sensor 1     65C/149F                 72C/161F',
                  'Controller 2 Sensor 2     70C/158F                 77C/170F',
                  'Controller 1 Sensor 3     78C/172F                 88C/190F',
                  'Controller 2 Sensor 4     65C/149F                 72C/161F',
                  'Controller 1 Sensor 5     70C/158F                 77C/170F',
                  'Controller 2 Sensor 6     78C/172F                 88C/190F'
                  ]
    for cp in checkpoint:
        if cp not in checkResult:
            FailFlag = True
            tolog('<font color="red"> Fail: factorydefaults -a restore -t encl </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t encl </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsFc(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'fc'):
        FailFlag =True
    checkResult = SendCmd(c, 'fc -v')
    checkpoint = ['ConfiguredLinkSpeed: Auto',
                  'ConfiguredTopology: Auto',
                  'HardALPA: ',
                  ]
    for cp in checkpoint:
        if cp not in checkResult:
            FailFlag = True
            tolog('<font color="red"> Fail: factorydefaults -a restore -t fc </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t fc </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsIscsi(c):
    FailFlag = False
    checkResult1 = SendCmd(c, 'iscsi -t session')
    if 'No session in the subsystem' in checkResult1:
        if factorydefaultsRestoreSetting(c, 'iscsi'):
            FailFlag = True
        checkResult2 = SendCmd(c, 'trunk')
        if 'No iSCSI trunks are available' not in checkResult2:
            FailFlag = True
            tolog('<font color="red"> Fail: factorydefaults -a restore -t iscsi </font>')
    else:
        tolog('\n<font color="red">Fail: Some iSCSI sessions are established on the portal </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t iscsi </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsPhydrv(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'phydrv'):
        FailFlag =True
    checkResult = SendCmd(c, 'phydrv -v')
    countPD = checkResult.count('-------------------------------------------------------------------------------')
    checkpoint = [checkResult.count('WriteCache: Enabled'),
                  checkResult.count('RlaCache: Enabled'),
                  checkResult.count('Alias: \r\n'),
                  checkResult.count('TempPollInt: 245'),
                  checkResult.count('MediumErrorThreshold: 64')
                  ]
    for cp in checkpoint:
        if cp != countPD:
            FailFlag = True
            tolog('<font color="red"> Fail: factorydefaults -a restore -t phydrv </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t phydrv </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsSas(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'sas'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t sas </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsScsi(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'scsi'):
        FailFlag =True


    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t scsi </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsSubsys(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'subsys'):
        FailFlag =True
    checkResult = SendCmd(c, 'subsys -v')
    if 'Alias:  ' not in checkResult or 'RedundancyType: Active-Active' not in checkResult or 'CacheMirroring: Enabled' not in checkResult:
        FailFlag = True
        tolog('<font color="red"> Fail: factorydefaults -a restore -t scsi </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t scsi </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsBgasched(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'bgasched'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t bgasched </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="red"> bgasched is not achieved </font>')
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsService(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'service'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t service </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsWebserver(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'webserver'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t webserver </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsSnmp(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'snmp'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t snmp </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsTelnet(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'telnet'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t telnet </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsSsh(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'ssh'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t ssh </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsEmail(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'email'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t email </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsCim(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'cim'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t cim </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsNtp(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'ntp'):
        FailFlag =True
    checkResult = SendCmd(c, 'ntp')
    if 'Ntp: Disabled' not in checkResult:
        FailFlag = True
        tolog('<font color="red"> Fail: factorydefaults -a restore -t ntp </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -a restore -t ntp </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsUser(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'user'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t user </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsUps(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'ups'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t ups </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsLdap(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'ldap'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t ldap </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def factorydefaultsSyslog(c):
    FailFlag = False
    if factorydefaultsRestoreSetting(c, 'syslog'):
        FailFlag =True

    if FailFlag:
        tolog('\n<font color="red">Fail: factorydefaults -a restore -t syslog </font>')
        tolog(Fail)
    else:
        tolog('\n<font color="green">Pass</font>')
        tolog(Pass)
def verifyFactorydefaultsHelp(c):
    FailFlag = False
    tolog("<b>Verify factorydefaults -h </b>")
    result = SendCmd(c, 'factorydefaults -h')
    if 'Error (' in result or 'restore' not in result:
        FailFlag = True
        tolog('\n<font color="red">Fail: factorydefaults -h </font>')
    if FailFlag:
        tolog('\n<font color="red">Fail: Verify factorydefaults -h </font>')
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
    factorydefaultsBga(c)
    factorydefaultsCtrl(c)
    factorydefaultsEncl(c)
    factorydefaultsFc(c)
    factorydefaultsIscsi(c)
    factorydefaultsPhydrv(c)
    factorydefaultsSas(c)
    factorydefaultsScsi(c)
    factorydefaultsSubsys(c)
    factorydefaultsBgasched(c)
    factorydefaultsService(c)
    factorydefaultsWebserver(c)
    factorydefaultsSnmp(c)
    factorydefaultsTelnet(c)
    factorydefaultsSsh(c)
    factorydefaultsEmail(c)
    factorydefaultsCim(c)
    factorydefaultsNtp(c)
    factorydefaultsUser(c)
    factorydefaultsUps(c)
    factorydefaultsLdap(c)
    factorydefaultsSyslog(c)
    verifyFactorydefaultsHelp(c)
    verifyFactorydefaultsInvalidOption(c)
    verifyFactorydefaultsInvalidParameters(c)
    verifyFactorydefaultsMissingParameters(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped