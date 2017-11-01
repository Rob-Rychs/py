import os, imapclient, pyzmail, pprint, time, subprocess, ctypes

password = input()

while True:
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login("rocks.ayush2011@gmail.com", password)
    imapObj.select_folder('INBOX', readonly=False)

    uids = imapObj.search(['FROM rocks.ayush2011@gmail.com', 'UNSEEN'])

    if len(uids) > 0:
        rawMessages = imapObj.fetch(uids, [b'BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[uids[0]][b'BODY[]'])
        subject = message.get_subject().strip()

        if(subject == 'Yo'):
            command = message.text_part.get_payload().decode(message.text_part.charset).strip()

            if command== 'play it':
                print('logging off......')
                subprocess.Popen(['start', 'alarm.mp3'], shell=True)

            if command == 'log off':
                print('logging off.....')
                ctypes.windll.user32.LockWorkStation()
            
    for i in range(10):
        time.sleep(1)
