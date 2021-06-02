import re 
import docx
  
  
filepath=r"C:\Users\Mani\OneDrive\Desktop\Interview\sample_resume.docx"  
  
def getMobileNumber(filepath):
    doc = docx.Document(filepath)
    list_items=[p.text for p in doc.paragraphs]
    string_items="".join(list_items)
    mobileNumberPattern = re.compile("[6-9][0-9]{9}")    
    return(mobileNumberPattern.search(string_items))
    
mobileNoFromResume=getMobileNumber(filepath)
if (mobileNoFromResume): 
  print("Mobile Number is present in the resume")
else: 
  print("Mobile Number is not present in the resume")

    


