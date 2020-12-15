import sys
sys.path.append('/home/jabrane/Downloads/pfa/project')
sys.path.append('/home/jabrane/Downloads/pfa/project/noteFinal')
sys.path.append('/home/jabrane/Downloads/pfa/project/recognition')

from Notes import noteExtraction
from Notes import digitSegmentation
from noteFinal import prePro
from recognition.model_02 import model02_performRec

note = ""
def main(File):
    noteExtraction.etap1(File)
    digitSegmentation.etape2()
    prePro.etape3()
    note = model02_performRec.etape4()
    return note



