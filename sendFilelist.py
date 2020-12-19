
import zipfile

import io,os
from pygit2 import Repository
import sendMailBase

if __name__ == '__main__':
    in_memory_zip = io.BytesIO()
    z = zipfile.ZipFile(in_memory_zip,'w',zipfile.ZIP_DEFLATED)
    flist=['syncapp.exe','nlog.dll','nlog.xml',
    'nlog.config','inifileparser.dll','inifileparser.xml',
    'watchdog.exe','worker3.dll','msvcr120.dll','datareader.exe']
    for a in flist:
        z.write(r'src/bin/release/'+a,a)

    z.close()


    print(Repository('.').head.shorthand)  # 'master'
    folder_path1 = os.getcwd()
    folder_path2 = os.getcwd().replace('\\','/')
    vl = folder_path1.split('\\')
    print(vl[-1])
    sendMailBase.sendMail_Zip(in_memory_zip,vl[-1])