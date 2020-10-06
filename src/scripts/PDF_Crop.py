
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader
from openpyxl.compat import file

def create_parsers():
    p = argparse.ArgumentParser(
        prog='crop',
        description='"%(prog)s" crop pdfs',
    )

    p.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input pdf',
    )

    p.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='Output pdf',
    )

    p.add_argument(
        '-b', '--bbox',
        type=float,
        nargs='*',
        required=True,
        help='Bounding box [y0 y1 x0 x1]',
    )

    return p


if __name__ == '__main__':

    p = create_parsers()
    args = p.parse_args()

    input_filename = args.input
    output_filename = args.output
    bounding_box = args.bbox

    input1 = PdfFileReader(file(input_filename, "rb"))
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print
        page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
        page.trimBox.lowerLeft = (bounding_box[0], bounding_box[2])
        page.trimBox.upperRight = (bounding_box[1], bounding_box[3])
        page.cropBox.lowerLeft = (bounding_box[0], bounding_box[2])
        page.cropBox.upperRight = (bounding_box[1], bounding_box[3])
        output.addPage(page)

    outputStream = file(output_filename, "wb")
    output.write(outputStream)
    outputStream.close()