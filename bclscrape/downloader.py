import requests
import os 
import time 
import PyPDF2
import re

here = os.path.dirname(__file__)
report_file = here + "/reports/"
sheets_file = here + "/balance_sheets/"

chunk_size = 2000

listo = ['https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2000.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2002.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2012/09/BCLAnnualReport20031.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2004.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2012/09/annual20051.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2006.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2007.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2014/09/BCL-AnnualReport20081.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport2009.pdf']

new_listo = ['https://www.bcl.com.pg/wp-content/uploads/2015/06/Annual-Report-2010.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/06/2011-Annual-Report.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/06/2012-Annual-Report.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/06/Bougainville-Copper-Limited-Annual-Report-2013.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/06/Bougainville-Copper-Limited-Annual-Report-2014.pdf', 'https://www.bcl.com.pg/wp-content/uploads/2015/06/2015-Annual-Report-Final.pdf']
listo = listo + new_listo
years = [2000, 2002, 2003, 2004, 2005, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
# for i in range(1990, 2000):
for b in range(0, len(years)):
    i = years[b]
    try:

        print(f"Count: {i}")

        # url = f'https://www.bcl.com.pg/wp-content/uploads/2015/07/BCL-AnnualReport{i}.pdf'
        url = listo[b]
        r = requests.get(url, stream=True)

        with open(f"{report_file}BCL-AnnualReport{i}.pdf", "wb") as f:
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
    except Exception as e:
        print(e)
        print(f"Count: {i}")
        continue

    time.sleep(2)

    # print("\n\n Now extracting \n\n")


    # file = f"{report_file}BCL-AnnualReport{i}.pdf"
    # print(file)

    # obj = PyPDF2.PdfFileReader(file)
    # string = "Current Assets"
    # num_pages = obj.getNumPages()

    # for b in range(0, num_pages):
    #     PageObj = obj.getPage(b)
    #     Text = PageObj.extractText()
    #     if re.search(string,Text):
    #         print("Pattern Found on Page: " + str(b))
    #         final_page = obj.getPage(b)

    #         pdf_writer = PyPDF2.PdfFileWriter()
    #         pdf_writer.addPage(final_page)

    #         with open(f"{sheets_file}{b}_balance_sheet.pdf", "wb") as f:
    #             pdf_writer.write(f)
        # else: 
        #     print(f"Couldn't find current assets in {i}")
    
    # time.sleep(2)