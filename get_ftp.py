# LETS TRY TO CONNECT TO THE FTP SITE AND GET THE FILES

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import ssl,smtplib,ftplib
from ftplib import FTP_TLS, FTP
import itertools
import socket
import sys
import urllib
import xmltodict
import json
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secretkey123'
)


@app.route('/')
def test():
    # current_time=datetime.datetime.now()
    #dict = ('nct_id': 'NCT01119859', 'title': 'This is a really good title!')
    dict = [('NCT01119859','This is a really good title!')]
    tup1 = ['NCT01119859', 'NCT09119859','NCT01119129']  # A LIST
    print('This is the Tup1 data type',type(tup1))
    tup2 = ['This is a really good title1!','This is a really good title2!','This is a really good title3!']
    print('This is the Tup2 data type',type(tup2))

    dir='NCT09119859'
    dirl=('NCT09119859','NCT01119129')

    dictionary = zip(tup1,tup2)
    print(type(dictionary) )
    print(dictionary)





    #WORKS SINGLE VALUE
    for i in range(0,len(tup1)):
        if tup1[i]==dir:
           x=tup2[i]

    #WORKS LIST
    y=[]
    for i in range(0,len(tup1)):
        for j in range(0,len(dirl)):
            if tup1[i]==dirl[j]:
               y.append(tup2[i])
               print(y)

    return render_template('test.html', **locals())





###################################
#LOG IN TO FTP SERVER
# client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# client_context.options |= ssl.OP_NO_TLSv1_1
# ftps = ftplib.FTP_TLS(source_address=('moveit.accenture.com',22),timeout=30)
# ftps.login('TCRomh01','3hEjc1T1')
# ftps.prot_p()
# #MOVE TO THE RIGHT FOLDER
# ftps.cwd('/SDTM Conversion Library/Converted Studies/')
# # # requests.get("moveit.accenture.com", timeout=5)
# # ftps.retrlines('LIST')
# ftps.quit()

# try:
#   # PRINT OUT THE DIRECTORY LISTING
#   data = []
#   ftps.dir(data.append)
#   ftps.quit()
# except socket.TimeoutError:
#     print >> sys.stderr, 'Retrying after TimeoutError'
#     print('I am here at this point')
#
# for line in data:
#     print ("-", line)

###################################

# def grabFile():
#
#     filename = 'example.txt'
#
#     localfile = open(filename, 'wb')
#     ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
#
#     ftp.quit()
#     localfile.close()
#

########################################

# class tyFTP(ftplib.FTP_TLS):
#   def __init__(self,
#                host='',
#                user='',
#                passwd='',
#                acct='',
#                keyfile=None,
#                certfile=None,
#                timeout=60):
#
#     ftplib.FTP_TLS.__init__(self,
#                             host=host,
#                             user=user,
#                             passwd=passwd,
#                             acct=acct,
#                             keyfile=keyfile,
#                             certfile=certfile,
#                             timeout=timeout)
#
#   def connect(self, host='', port=0, timeout=-999):
#     """Connect to host.  Arguments are:
#     - host: hostname to connect to (string, default previous host)
#     - port: port to connect to (integer, default previous port)
#     """
#     if host != '':
#         self.host = host
#     if port > 0:
#         self.port = port
#     if timeout != -999:
#         self.timeout = timeout
#     try:
#         self.sock = socket.create_connection((self.host, self.port), self.timeout)
#         self.af = self.sock.family
#         # add this line!!!
#         self.sock = ssl.wrap_socket(self.sock,
#                                     self.keyfile,
#                                     self.certfile,
#                                     ssl_version=ssl.PROTOCOL_TLSv1)
#         # add end
#         self.file = self.sock.makefile('rb')
#         self.welcome = self.getresp()
#     except Exception as e:
#         print(e)
#     return self.welcome
#
#####################################################
# server = tyFTP()
# server.connect(host="moveit.accenture.com", port=22)
# server.login(user="TCRomh01", passwd="3hEjc1T1")
# server.prot_p()
# server.cwd('/SDTM Conversion Library/Converted Studies/')

# class ImplicitFTP_TLS(ftplib.FTP_TLS):
#     """FTP_TLS subclass that automatically wraps sockets in SSL to support implicit FTPS."""
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._sock = None
#
#     @property
#     def sock(self):
#         """Return the socket."""
#         return self._sock
#
#     @sock.setter
#     def sock(self, value):
#         """When modifying the socket, ensure that it is ssl wrapped."""
#         if value is not None and not isinstance(value, ssl.SSLSocket):
#             value = self.context.wrap_socket(value)
#         self._sock = value
#
# ftp_client = ImplicitFTP_TLS()
# ftp_client.connect(host='moveit.accenture.com', port=22)
# ftp_client.login(user="TCRomh01", passwd="3hEjc1T1")
# ftp_client.prot_p()
# ftp_client.cwd('/SDTM Conversion Library/Converted Studies/')


######################################################

#from ftplib import FTP_TLS, FTP
#import socket


# class IMPLICIT_FTP_TLS(FTP_TLS):
#     def __init__(self, host='', user='', passwd='', acct='', keyfile=None,
#         certfile=None, timeout=60):
#         FTP_TLS.__init__(self, host, user, passwd, acct, keyfile, certfile, timeout)
#
#     def connect(self, host='', port=0, timeout=-999):
#         '''Connect to host.  Arguments are:
#         - host: hostname to connect to (string, default previous host)
#         - port: port to connect to (integer, default previous port)
#         '''
#         if host != '':
#             self.host = host
#         if port > 0:
#             self.port = port
#         if timeout != -999:
#             self.timeout = timeout
#         try:
#             self.sock = socket.create_connection((self.host, self.port), self.timeout)
#             self.af = self.sock.family
#             self.sock = ssl.wrap_socket(self.sock, self.keyfile, self.certfile)
#             self.file = self.sock.makefile('rb')
#             self.welcome = self.getresp()
#         except Exception as e:
#             print (e)
#         return self.welcome
#
#     def ntransfercmd(self, cmd, rest=None):
#         conn, size = FTP.ntransfercmd(self, cmd, rest)
#         if self._prot_p:
#             conn = ssl.wrap_socket(conn, self.keyfile, self.certfile)
#         return conn, size
#
# ftps = IMPLICIT_FTP_TLS()
# ftps.connect(host='moveit.accenture.com', port=22)
# ftps.login(user="TCRomh01", passwd="3hEjc1T1")
# ftps.prot_p()
# ftps.retrlines('LIST')



if __name__ == '__main__':
    app.run('0.0.0.0',5001,debug=True)
