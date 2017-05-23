# -*- coding: utf-8 -*-

import time


def tolog(strinfo):
        if strinfo!="'result': 'p'" or strinfo!="'result': 'f'":
<<<<<<< HEAD
            with open("/home/work/jackyl/Scripts/clitest/cli_scripts.log", "r+") as f:
            #with open("./cli_scripts.log", "r+") as f:
=======
            with open("cli_scripts.log", "r+") as f:
>>>>>>> e35cc64ae7b64174c9c9163e88bac77aaddcd153
                content = f.read()
                f.seek(0, 0)
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(time.time())) + ": " + strinfo + '\n' + content)

                f.close()
            print(strinfo)
        # for testlink steps populate
<<<<<<< HEAD
        fout=open("/home/work/jackyl/Scripts/clitest/testlink.notes","a")
=======
        fout = open("testlink.notes","a")
>>>>>>> e35cc64ae7b64174c9c9163e88bac77aaddcd153
        fout.write(strinfo+ '\n')

        fout.close()


