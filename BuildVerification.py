# initial version
# March 16, 2017
# architecture
# 1. getnewbuild from buildserver
# 2. scp to tftpserver
# 3. login to hypersion-DS console, execute
#    ptiflash -t -s 10.84.2.99 -f d5k-multi-12_0_9999_xx.ptif
#    ptiflash -t -s 10.84.2.99 -f d5k-conf-12_0_9999_48.ptif
# 4. execute auto script for cli and webgui
# 5. send email according to the test result

buildserverurl="http://192.168.208.5/release/hyperion_ds/daily/"
tftpserver="root@10.84.2.99:/work/tftpboot/"
import pool
from time import sleep

import os

from send_cmd import *
from ssh_connect import *
import bbm
forBVT = True
from to_log import *
import buzzer
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def BuildVerification(c):
    Failflaglist=list()
    flashimage=False
    c, ssh = ssh_conn()

    versioninfo = SendCmd(c, "about")

    currentbuild = versioninfo.split("Version: ")[1][:13]



    tftpbuildnumber=open("/home/work/jackyl/Scripts/clitest/buildnum","r").readline().rstrip()
    print "currentbuild,",currentbuild
    print "tftpbuildnumber,",tftpbuildnumber

    if ("13." in currentbuild and "13." in tftpbuildnumber) and (int(currentbuild.split(".")[-1])<int(tftpbuildnumber.split(".")[-1])) or (
        "12.00" in currentbuild and "12.0" in tftpbuildnumber) and (
        int(currentbuild.split(".")[-1]) < int(tftpbuildnumber.split(".")[-1])) or (
        "12.01" in currentbuild and "12.1" in tftpbuildnumber) and (
        int(currentbuild.split(".")[-1]) < int(tftpbuildnumber.split(".")[-1])) or (
        "12.00" in currentbuild and "12.1" in tftpbuildnumber):
        #filename="d5k-multi-13_0_0000_"+tftpbuildnumber.split(".")[-1]
        if "13." in tftpbuildnumber:

            filename = "d5k-multi-13_0_0000_" + tftpbuildnumber.split(".")[-1]
        elif "12.0" in tftpbuildnumber:

            filename = "d5k-multi-12_0_9999_" + tftpbuildnumber.split(".")[-1]
        elif "12.1" in tftpbuildnumber:

            filename = "d5k-multi-12_1_9999_" + tftpbuildnumber.split(".")[-1]

        tolog("%s will be updated to the %s" % (filename, server))
        flashimage = True
        SendCmdRestart(c,"ptiflash -y -t -s 10.84.2.99 -f "+filename+".ptif")




    if flashimage:
        i=1
        while i< 160:
            # wait for rebooting
           tolog("ptiflash is in progress, please wait, %d seconds elapse" %i)
           i+=1
           sleep(1)

    # check if ssh connection is ok.
    # wait for another 40 seconds
        reconnectflag=False
        for x in range(30):
            try:
                c,ssh=ssh_conn()
                reconnectflag=True
                break
            except Exception, e:
                print e
                sleep(4)


        if reconnectflag:
            tolog("Start verifying pool add")
            Failflaglist.append(pool.bvtpoolcreateandlist(c,1))
            
            tolog("Start verifying pool global setting")
            Failflaglist.append(pool.bvtpoolglobalsetting(c))

            tolog("Start verifying volume add")
            Failflaglist.append(pool.bvtvolumecreateandlist(c,10))

            tolog("Start verifying snapshot add")
            Failflaglist.append(pool.bvtsnapshotcreateandlist(c,2))

            tolog("Start verifying clone add")
            Failflaglist.append(pool.bvtclonecreateandlist(c,2))


            tolog("Start verifying delete clone")
            Failflaglist.append( pool.bvtclonedelete(c))

            tolog("Start verifying delete snapshot")
            Failflaglist.append( pool.bvtsnapshotdelete(c))

            tolog("Start verifying delete volume")
            Failflaglist.append( pool.bvtvolumedel(c))

            tolog("Start verifying delete pool")
            Failflaglist.append(pool.bvtpooldel(c))


            tolog("Start verifying pool add")
            Failflaglist.append(pool.bvtpoolcreateandlist(c, 0))

            tolog("Start verifying pool global setting")
            Failflaglist.append(pool.bvtpoolglobalsetting(c))

            tolog("Start verifying volume add")
            Failflaglist.append(pool.bvtvolumecreateandlist(c, 5))

            tolog("Start verifying volume add many")
            Failflaglist.append(pool.bvtvolumeaddmany(c, 5))

            tolog("Start verifying snapshot add")
            Failflaglist.append(pool.bvtsnapshotcreateandlist(c, 2))

            tolog("Start verifying clone add")
            Failflaglist.append(pool.bvtclonecreateandlist(c, 2))

            tolog("Start verifying clone force delete")
            Failflaglist.append(pool.bvtforcedel(c, "clone"))

            tolog("Start verifying snapshot force delete")
            Failflaglist.append(pool.bvtforcedel(c, "snapshot"))

            tolog("Start verifying volume force delete")
            Failflaglist.append(pool.bvtforcedel(c, "volume"))

            tolog("Start verifying pool force delete")
            Failflaglist.append(pool.bvtforcedel(c, "pool"))

            tolog("Start verifying pool add")
            Failflaglist.append(pool.bvtpoolcreateandlist(c, 2))

            tolog("Start verifying spare add")
            Failflaglist.append(pool.bvtsparedrvcreate(c, 2))

            tolog("Start verifying delete spare")
            Failflaglist.append(pool.bvtsparedelete(c))

            tolog("Start verifying pool extend")
            Failflaglist.append(pool.bvtpoolmodifyandlist(c))

            Failflaglist.append(pool.bvtforcedel(c, "pool"))

            tolog("Start verifying pool create with all raid level and parameters")
            Failflaglist.append(pool.bvtpoolcreateverify_newraidlevel(c))


            tolog("Start verifying pool output error")
            Failflaglist.append(pool.bvtpoolcreateverifyoutputerror_newraidlevel(c))

            tolog("Start verifying buzzer")
            
            Failflaglist.append(buzzer.bvt_verifyBuzzerDisableAndSilentTurnOn((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSilentTurnOn((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSoundingTurnOn((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerDisableAndSilentTurnOff((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSilentTurnOff((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSoundingTurnOff((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerDisableAndSilentEnable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSilentEnable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSoundingEnable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSoundingDisable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerEnableAndSilentDisable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerDisableAndSilentDisable((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerInfo((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerHelp((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerInvalidParameters((c)))
            Failflaglist.append(buzzer.bvt_verifyBuzzerInvalidOption((c)))

            tolog("Start verifying BBM")
            Failflaglist.append(bbm.bvt_verifyBBM(c))

            Failflaglist.append(bbm.bvt_verifyBBMClear(c))

            Failflaglist.append(bbm.bvt_verifyBBMClearFailedTest(c))

            Failflaglist.append(bbm.bvt_verifyBBMHelp(c))

            Failflaglist.append(bbm.bvt_verifyBBMInvalidOption(c))

            Failflaglist.append(bbm.bvt_verifyBBMInvalidParameters(c))

            Failflaglist.append(bbm.bvt_verifyBBMList(c))

            Failflaglist.append(bbm.bvt_verifyBBMMissingParameters(c))

            Failflaglist.append(bbm.bvt_verifyBBMSpecifyInexistentId(c))

            import ctrl
            tolog("Start verifying ctrl")
            Failflaglist.append(ctrl.bvt_verifyCtrl(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlSpecifyId(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlSpecifyInexistentId(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlList(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlV(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlListV(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlModNormativeAlias(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlModValuesIsEnableOrDisable(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlModValuesIsTime(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlClear(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlHelp(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlInvalidOption(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlInvalidParameters(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlMissingParameters(c))
            Failflaglist.append(ctrl.bvt_verifyCtrlSpecifyInexistentId(c))

        else:
            tolog("Failed to connect server after ptiflash.")
            Failflaglist.append(True)

        for flag in Failflaglist:
            if Failflaglist:
                tolog(Fail)
                break
            else:
                tolog(Pass)
    else:
        tolog("no new build is availlable.")
        tolog(Pass)

    c.close()
def About(c):
    SendCmd(c,"about")
    tolog(Pass)
if __name__ == "__main__":

    start=time.clock()
    c,ssh=ssh_conn()
    BuildVerification(c)
    c.close()
