#!/usr/bin/python

import ftplib
import sys


server = sys.argv[1]
if len(sys.argv) == 2:
    ftp = ftplib.FTP(server)
    try:
        ftp.login()
    except ftplib.all_errors as e:
        print e
        sys.exit()
    print ftp.getwelcome()
    print 'Listing files and folders...'
    print ftp.retrlines('LIST')
elif len(sys.argv) == 4:
    user = sys.argv[2]
    passwd = sys.argv[3]
    ftp = ftplib.FTP(server)
    try:
        ftp.login(user, passwd)
    except ftplib.all_errors as e:
        print e
        sys.exit()
    print ftp.getwelcome()
    print 'Listing files and folders...'
    print ftp.retrlines('LIST')
else:
    print 'Usage: ' + sys.argv[0] + ' ' + 'server_name ' + '[username] ' + '[password]'
    sys.exit()


def cwd(cmd):     
        index = len('CWD') + 1
        dir_name = cmd[index:]
        ftp.cwd(dir_name)
        print ftp.retrlines('LIST')

def download(cmd):
    index = len('RETR') + 1
    filename = cmd[index:]
    f = open(filename,"wb")
    print ftp.retrbinary('RETR %s' % filename, f.write)
    f.close()

def upload(cmd):
    index = len('STOR') + 1
    filename = cmd[index:]
    f = open(filename, "rb")
    print ftp.storbinary('STOR %s' % filename, f)
    f.close()

def delete(cmd):
    index = len('DELE') + 1
    filename = cmd[index:]
    print ftp.delete(filename)

    
    


while ftp:
    try:
        cmd = raw_input('ftp> ')
    except KeyboardInterrupt:
        sys.exit()
    if cmd.startswith('CWD'):
        cwd(cmd)
    elif cmd.startswith('RETR'):
        download(cmd)
    elif cmd.startswith('PWD'):
        print 'Current directory path: '
        print ftp.pwd()
    elif cmd.startswith('STOR'):
        upload(cmd)
    elif cmd.startswith('LIST'):
        print ftp.retrlines('LIST')
    elif cmd.startswith('DELE'):
        delete(cmd)
    elif cmd.startswith('QUIT'):
        print ftp.quit()
        sys.exit()
       

    


