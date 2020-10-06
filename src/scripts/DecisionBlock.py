from tika import parser
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfdevice import PDFDevice
from PDF2PNG_w_GUI import pdf2png_gui
from Table_Crop import table_crop

# def make_decision(filepath):
# Open a PDF file.
def make_decision_scanned_searchable(filepath):
    # filepath = r'C:\Users\Pratik\PycharmProjects\SIH2019\JP Morgan Scanned.pdf'


    raw = parser.from_file(filepath)
    raw = raw['content']
    print (raw)

    if not raw:

        print('SCANNED PDF')
        pdf2png_gui()
        table_crop()



        #raise PDFTextExtractionNotAllowed
        #CODE BLOCK FOR SCANNED PDF

        #Step1. Goes to PDF2PNG
        #Step2. Table_crop
        #Step3. OCR
        #Step4. Extract tabular data using tabula
        #Done

    else:
        print ('SEARCHABLE PDF')



        #CODE BLOCK FOR SEARCHABLE PDF

        #Step1: PDF_Split
        #Step2: PDF_Crop #output in cropped searchable pdf
        #Step3: Output of step2 act as an input to Tabula to extract table/
        #Done


