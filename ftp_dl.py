# LETS TRY TO CONNECT TO THE FTP SITE AND GET THE FILES

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import ftplib
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


# FUNCTION EXTRACT THE DATA FROM CLINICALTRIAL.GOV BASED ON NCT_ID
def get_CT_info(nct_id):
    file = urllib.request.urlopen('https://clinicaltrials.gov/ct2/show/'+nct_id+'?displayxml=true')
    data = file.read()
    file.close()

    #CONVERT XML TO DICT THEN TO JSON FORMAT
    data = xmltodict.parse(data)
    data2=json.dumps(data)
    d = json.loads(data2)
    #SAVE THE FILE FOR FUTURE USE
    with open(os.path.join('.\json',nct_id+'.json'), 'w') as fp:
         json.dump(d,fp)
    return


# READ IN LIST OF NCT AND GET THE INFO FROM CLINICLATRIAL.GOV
# f = open('nctlist.txt')
# print(f)
# lines = f.read().splitlines()
# for line in lines:
#     get_CT_info(line)
#     f.close()

def extract_NCT(nct_id):
    jsonfile=os.path.join('.\json',nct_id+'.json')
    # infile=os.path.join('.\json',nct_id+'.json')
    # print(type(infile))
    # d=json.loads(infile)
    print('jsonfile', type(jsonfile) )#STR
    print(jsonfile)
    with open(jsonfile) as data_file:
         data = json.load(data_file)
         print('What is the type of data? ',type(data))
         print (data['clinical_study']['brief_title'])
         print ('The NCT number?',data['clinical_study']['id_info']['nct_id'])
         title =data['clinical_study']['brief_title']
         nct_id=data['clinical_study']['id_info']['nct_id']
    return title, nct_id

get_CT_info('NCT01119859')
#
#extract_NCT('NCT01119859')


@app.route('/')
def home():
    nct_id,title=extract_NCT('NCT01119859')
    return render_template('home.html', **locals())


    # file = urllib.request.urlopen('https://clinicaltrials.gov/ct2/show/NCT01119859?displayxml=true')
    # data = file.read()
    # file.close()

    # ALL THE XML AS AN OBJECT
    # data = xmltodict.parse(data)

    # data2=json.dumps(xmltodict.parse(data),indent=4)
    # data2=xmltodict.parse(data)
    # print ('--------')
    # type(data2)
    # for key in data2:
    #     print(key, data2['clinical_study'])
    # print (data2['clinical_study']['brief_title'])
    # print ([d['clinical_study'] for d in data2])


#LOG IN TO FTP SERVER
# ftp = ftplib.FTP('moveit.accenture.com')
# ftp.login('TCRomh01','3hEjc1T1')
# ftp = ftplib.FTP("www.python.org")
# ftp.login("anonymous", "ftplib-example-1")
#MOVE TO THE RIGHT FOLDER
# ftp.cwd('/SDTM /')

# try:
#   # PRINT OUT THE DIRECTORY LISTING
#   data = []
#   ftp.dir(data.append)
#   ftp.quit()
# except socket.TimeoutError:
#   print >> sys.stderr, 'Retrying after TimeoutError'
#   dosomething()
#
# for line in data:
#     print ("-", line)



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
if __name__ == '__main__':
    app.run('0.0.0.0',5001,debug=True)
