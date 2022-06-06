import PyPDF2
import os
import re


def get_subject_from_info(plRead):
    info = plRead.getDocumentInfo()
    if info.subject is None:
        return None
    subject = info.subject.strip()
    if subject == '':
        return None
    return subject


def get_subject_from_first_page(plRead):
    getpage = plRead.getPage(1)
    text = getpage.extractText()
    if text == '':
        return None
    return text.splitlines()[0].strip()


for fileName in os.listdir('..'):
    if fileName.endswith('.pdf'):
        shortName = fileName[0:-4]
        if len(shortName) > 10:
            continue
        try:
            pl = open(fileName, 'rb')

            plRead = PyPDF2.PdfFileReader(pl)
            if plRead is None:
                continue

            subject = get_subject_from_info(plRead)
            if subject is None:
                subject = get_subject_from_first_page(plRead)

            if subject == '':
                continue

            if subject is None:
                continue

            if len(subject) > 50:
                continue

            # print(subject)
            # continue

            # print('%s: %s' % (fileName, subject));
            pl.close()

            newFileName = re.sub('[^\w_.)( -]', '_', subject)
            print(newFileName)
            os.rename(fileName, "%s.pdf" % newFileName)
        except:
            continue
