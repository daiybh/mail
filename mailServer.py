from __future__ import print_function
from datetime import datetime
import asyncore
import smtpd
import io
import sys
from smtpd import SMTPServer

smtpd.DEBUGSTREAM = sys.stdout
class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        
        self.no += 1
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
          
        print('\n\n%s saved.\n\n\n' % filename)      
        return
        f = open(filename, 'w')
        f.write(data)
        f.close


def run():
    # start the smtp server on localhost:1025
    foo = EmlServer(('192.168.21.3', 31025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()