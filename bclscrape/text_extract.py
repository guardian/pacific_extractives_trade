import PyPDF2
import os 
import re

here = os.path.dirname(__file__)
report_file = here + "/reports/"
sheets_file = here + "/balance_sheets/"
summaries_file = here + "/statistical_summaries/"

# strings_to_check = ["Balance sheet", "Statement of comprehensive income", 'Statement of cash flows']
strings_to_check = ["Statistical summary"]
file = '/Users/josh/Dropbox/Coding/graun/bclscrape/test.pdf'

for year in range(1966, 2015):
    print(f"Starting: {year}")

    file = f"{report_file}BCL-AnnualReport{year}.pdf"

    if os.path.isfile(file):

        obj = PyPDF2.PdfFileReader(file)
        num_pages = obj.getNumPages()

        pdf_writer = PyPDF2.PdfFileWriter()

        for string in strings_to_check:
            print(f"Checking: {string}\n")

            for i in range(0, num_pages):
                PageObj = obj.getPage(i)
                Text = PageObj.extractText().lower()
                if re.search(string.lower(),Text):
                    print("Pattern Found on Page: " + str(i))
                    final_page = obj.getPage(i)
                    pdf_writer.addPage(final_page)

    else:
        print(f"{year} wasn't a file")
        continue

    # with open(f"{sheets_file}sheets_{year}.pdf", "wb") as f:
    with open(f"{summaries_file}summaries_{year}.pdf", "wb") as f:
        pdf_writer.write(f)