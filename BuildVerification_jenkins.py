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
tftpserver="/work/tftpboot/"
import pool
from time import sleep

import os

from send_cmd import *
from ssh_connect import *
forBVT = True
from to_log import *
import bbm
Pass = "'result': 'p'"
Fail = "'result': 'f'"

def BuildVerification(c):
    Failflaglist=list()
    flashimage=False
    c, ssh = ssh_conn()

    import glob
    files=glob.glob("/var/lib/jenkins/workspace/HyperionDS/build/build/*.ptif")
    for file in files:


        filename=file.replace("/var/lib/jenkins/workspace/HyperionDS/build/build/","")
        SendCmdRestart(c,"ptiflash -y -t -s 10.84.2.66 -f "+filename)

        i=1
        while i< 160:
            # wait for rebooting
           tolog("ptiflash is in progress, please wait, %d seconds elapse" %i)
           i+=1
           sleep(1)

    # check if ssh connection is ok.
    # wait for another 120 seconds
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
        Failflaglist.append(pool.bvtpoolcreateandlist(c, 1))

        tolog("Start verifying pool global setting")
        Failflaglist.append(pool.bvtpoolglobalsetting(c))

        tolog("Start verifying volume add")
        Failflaglist.append(pool.bvtvolumecreateandlist(c, 10))

        tolog("Start verifying snapshot add")
        Failflaglist.append(pool.bvtsnapshotcreateandlist(c, 2))

        tolog("Start verifying clone add")
        Failflaglist.append(pool.bvtclonecreateandlist(c, 2))

        tolog("Start verifying spare add")
        Failflaglist.append(pool.bvtsparedrvcreate(c, 2))

        tolog("Start verifying delete clone")
        Failflaglist.append(pool.bvtclonedelete(c))

        tolog("Start verifying delete snapshot")
        Failflaglist.append(pool.bvtsnapshotdelete(c))

        tolog("Start verifying delete volume")
        Failflaglist.append(pool.bvtvolumedel(c))

        tolog("Start verifying delete pool")
        Failflaglist.append(pool.bvtpooldel(c))

        tolog("Start verifying delete spare")

        Failflaglist.append(pool.bvtsparedelete(c))

        tolog("Start verifying pool add")
        Failflaglist.append(pool.bvtpoolcreateandlist(c, 0))

        tolog("Start verifying pool global setting")
        Failflaglist.append(pool.bvtpoolglobalsetting(c))

        tolog("Start verifying volume add many")
        Failflaglist.append(pool.bvtvolumeaddmany(c, 5))

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


        Failflaglist.append(bbm.bvt_verifyBBM(c))

        Failflaglist.append(bbm.bvt_verifyBBMClear(c))

        Failflaglist.append(bbm.bvt_verifyBBMClearFailedTest(c))

        Failflaglist.append(bbm.bvt_verifyBBMHelp(c))

        Failflaglist.append(bbm.bvt_verifyBBMInvalidOption(c))

        Failflaglist.append(bbm.bvt_verifyBBMInvalidParameters(c))

        Failflaglist.append(bbm.bvt_verifyBBMList(c))

        Failflaglist.append(bbm.bvt_verifyBBMMissingParameters(c))

        Failflaglist.append(bbm.bvt_verifyBBMSpecifyInexistentId(c))


    else:
        tolog("Failed to connect server after ptiflash.")
        Failflag = True
    for Failflag in Failflaglist:

        if Failflag:
            tolog(Fail)
            break
        else:
            tolog(Pass)


    c.close()
    ssh.close()
if __name__ == "__main__":

    start=time.clock()
    c,ssh=ssh_conn()
    BuildVerification(c)
    c.close()