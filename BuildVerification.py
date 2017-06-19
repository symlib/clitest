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

            tolog("Start verifying spare add")
            Failflaglist.append( pool.bvtsparedrvcreate(c, 2))

            tolog("Start verifying delete clone")
            Failflaglist.append( pool.bvtclonedelete(c))

            tolog("Start verifying delete snapshot")
            Failflaglist.append( pool.bvtsnapshotdelete(c))

            tolog("Start verifying delete volume")
            Failflaglist.append( pool.bvtvolumedel(c))

            tolog("Start verifying delete pool")
            Failflaglist.append(pool.bvtpooldel(c))

            tolog("Start verifying delete spare")
            Failflaglist.append(pool.bvtsparedelete(c))

            tolog("Start verifying pool add")
            Failflaglist.append(pool.bvtpoolcreateandlist(c, 0))

            tolog("Start verifying pool global setting")
            Failflaglist.append(pool.bvtpoolglobalsetting(c))

            tolog("Start verifying volume add")
            Failflaglist.append(pool.bvtvolumecreateandlist(c, 5))

            tolog("Start verifying snapshot add")
            Failflaglist.append(pool.bvtsnapshotcreateandlist(c, 2))

            tolog("Start verifying clone add")
            Failflaglist.append(pool.bvtclonecreateandlist(c, 2))

            tolog("Start verifying clone force delete")
            Failflaglist.append(pool.bvtforcedelete(c, "clone"))

            tolog("Start verifying snapshot force delete")
            Failflaglist.append(pool.bvtforcedelete(c, "snapshot"))

            tolog("Start verifying volume force delete")
            Failflaglist.append(pool.bvtforcedelete(c, "volume"))

            tolog("Start verifying pool force delete")
            Failflaglist.append(pool.bvtforcedelete(c, "pool"))

            tolog("Start verifying buzzer")
            
            Failflaglist.append(buzzer.BVTverifyBuzzerDisableAndSilentTurnOn((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSilentTurnOn((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSoundingTurnOn((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerDisableAndSilentTurnOff((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSilentTurnOff((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSoundingTurnOff((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerDisableAndSilentEnable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSilentEnable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSoundingEnable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSoundingDisable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerEnableAndSilentDisable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerDisableAndSilentDisable((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerInfo((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerHelp((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerInvalidParameters((c)))
            Failflaglist.append(buzzer.BVTverifyBuzzerInvalidOption((c)))
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
