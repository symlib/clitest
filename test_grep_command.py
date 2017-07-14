# coding=utf-8
# initial work on 2017.2.20
# this section includes list pd
from send_cmd import *
from ssh_connect import ssh_conn

def test_grep_command(c):
    list_no_grep = []
    vList_no_grep =[]
    command = ["about", "battery", "bbm", "bga", "buzz",  "chap", "clone", "ctrl", "date", "encldiag",
<<<<<<< HEAD
                "enclosure", "event", "export", "factorydefaults", "fc", "import", "initiator", "iscsi",
=======
                "enclosure", "event", "export", "factorydefaul", "fc", "import", "initiator", "iscsi",
>>>>>>> 785374210ab481e9a192d85a0c0c53bd7ab7ce01
                "isns", "logout", "lunmap", "maintenance", "net", "ntp", "password", "pcie", "perfstats",
                "phydrv", "ping", "pool", "ptiflash", "rb", "rc", "rcache", "sc", "session", "shutdown",
                "smart", "snapshot", "spare", "stats", "subscription", "subsys", "swmgt", "sync",
                "topology", "trunk", "ups", "user", "volume", "wcache"]


    for com in command:
        result = SendCmd(c, com + ' -h')
<<<<<<< HEAD
        if 'list' in result:
=======
        if 'list' in result and '(Default)' in result:
>>>>>>> 785374210ab481e9a192d85a0c0c53bd7ab7ce01
            grepListResult = SendCmd(c, com + ' | grep Aaaaaaaaaaaaa')
            if len(grepListResult) != len(com + ' | grep Aaaaaaaaaaaaa') + 23:
                list_no_grep.append(com)

            grepVListResult = SendCmd(c, com + ' -v | grep Aaaaaaaaaaaaa')
            if 'Error (' not in grepVListResult:
                if len(grepVListResult) != len(com + ' -v | grep Aaaaaaaaaaaaa') + 23:
                    vList_no_grep.append(com)
    print list_no_grep
    print vList_no_grep

if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    test_grep_command(c)
    ssh.close()
    elasped = time.clock() - start
    print "Elasped %s" % elasped