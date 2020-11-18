import pyttsx3
import PyPDF2

book_name = input("Enter the name of book:")
address_of_the_folder = input("Enter the Location of the folder:")
page_no = int(input("Enter the page number:"))
location_book = address_of_the_folder+"\\"+book_name

book =  open(location_book,"rb")
pdfReader = PyPDF2.PdfFileReader(book)
no_pages = pdfReader.numPages
print(no_pages)
speaker = pyttsx3.init()

for i in range(page_no-1,no_pages): 
    speaker.say(f"You are on page number {i} ")
    speaker.runAndWait()
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)  
    speaker.runAndWait()

 



