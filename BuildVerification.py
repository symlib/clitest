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
forBVT = True
from to_log import *
import buzzer
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def BuildVerification(c):
    Failflag=list()
    flashimage=False
    c, ssh = ssh_conn()

    versioninfo = SendCmd(c, "about")

    currentbuild = versioninfo.split("Version: ")[1][:13]



    tftpbuildnumber=open("/home/work/jackyl/Scripts/clitest/buildnum","r").readline().rstrip()
    print "currentbuild,",currentbuild
    print "tftpbuildnumber,",tftpbuildnumber

    if ("13." in currentbuild and "13." in tftpbuildnumber) and (int(currentbuild.split(".")[-1])<int(tftpbuildnumber.split(".")[-1])) or (
        "12.00" in currentbuild and "12.00" in tftpbuildnumber) and (
        int(currentbuild.split(".")[-1]) < int(tftpbuildnumber.split(".")[-1])) or (
        "12.01" in currentbuild and "12.01" in tftpbuildnumber) and (
        int(currentbuild.split(".")[-1]) < int(tftpbuildnumber.split(".")[-1])) or (
        "12.00" in currentbuild and "12.01" in tftpbuildnumber):
        #filename="d5k-multi-13_0_0000_"+tftpbuildnumber.split(".")[-1]
        if "13." in tftpbuildnumber:

            filename = "d5k-multi-13_0_0000_" + tftpbuildnumber.split(".")[-1]
        elif "12.00" in tftpbuildnumber:

            filename = "d5k-multi-12_0_9999_" + tftpbuildnumber.split(".")[-1]
        elif "12.01" in tftpbuildnumber:

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
            except Exception, e:
                print e
                sleep(4)


        if reconnectflag:
            tolog("Start verifying pool add")
            Failflag.append(pool.bvtpoolcreateandlist(c,1))

            tolog("Start verifying volume add")
            Failflag.append(pool.bvtvolumecreateandlist(c,10))

            tolog("Start verifying snapshot add")
            Failflag.append(pool.bvtsnapshotcreateandlist(c,2))

            tolog("Start verifying clone add")
            Failflag.append(pool.bvtclonecreateandlist(c,2))

            tolog("Start verifying spare add")
            Failflag.append( pool.bvtsparedrvcreate(c, 2))

            tolog("Start verifying delete clone")
            Failflag.append( pool.bvtclonedelete(c))

            tolog("Start verifying delete snapshot")
            Failflag.append( pool.bvtsnapshotdelete(c))

            tolog("Start verifying delete volume")
            Failflag.append( pool.bvtvolumedel(c))

            tolog("Start verifying delete pool")
            Failflag.append(pool.bvtpooldel(c))

            tolog("Start verifying delete spare")
            Failflag.append(pool.bvtsparedelete(c))

            tolog("Start verifying buzzer")
            Failflag.append(buzzer.BVTverifyBuzzerDisableAndSilentTurnOn((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSilentTurnOn((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSoundingTurnOn((c)))
            Failflag.append(buzzer.BVTverifyBuzzerDisableAndSilentTurnOff((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSilentTurnOff((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSoundingTurnOff((c)))
            Failflag.append(buzzer.BVTverifyBuzzerDisableAndSilentEnable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSilentEnable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSoundingEnable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSoundingDisable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerEnableAndSilentDisable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerDisableAndSilentDisable((c)))
            Failflag.append(buzzer.BVTverifyBuzzerInfo((c)))
            Failflag.append(buzzer.BVTverifyBuzzerHelp((c)))
            Failflag.append(buzzer.BVTverifyBuzzerInvalidParameters((c)))
            Failflag.append(buzzer.BVTverifyBuzzerInvalidOption((c)))
        else:
            tolog("Failed to connect server after ptiflash.")
            Failflag.append(True)

        for flag in Failflag:
            if Failflag:
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
