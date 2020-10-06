import requests
import response
import urllib.request
import json
from os.path import basename

def ocr_space_file(filename, isSearchablePdfHideTextLayer=False, api_key='8a8e61b0d788957', language='eng'):
    payload = {'isSearchablePdfHideTextLayer':isSearchablePdfHideTextLayer,
               'apikey': api_key,
               'language': language,
               'isCreateSearchablePdf': True,
               'scale': True,
               'isTable': True,
               'detectOrientation': True,

               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )

    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='8a8e61b0d788957', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


file_name = 'Citibank_Crop.png'
#file_name = 'Morgan Stanley_Crop.png'
#file_name = 'UBS Global_Crop.png'

temp_fn = basename(file_name).replace('.png','')
print('Applying OCR on ', temp_fn)


test_file_ocr = json.loads(ocr_space_file(filename=file_name, language='eng',  isSearchablePdfHideTextLayer=True))
test_file_overlay = json.loads(ocr_space_file(filename=file_name, language='eng',))


file_url_ocr = test_file_ocr['SearchablePDFURL']
file_url_overlay = test_file_overlay['SearchablePDFURL']



print('Beginning to download the file...')

urllib.request.urlretrieve(file_url_ocr, r'C:\Users\Pratik\PycharmProjects\SIH2019\OCR_Docs\\'+temp_fn+'_ocr.pdf')
urllib.request.urlretrieve(file_url_overlay, r'C:\Users\Pratik\PycharmProjects\SIH2019\OCR_Docs\\'+temp_fn+'_overlay.pdf')



print("Done!")