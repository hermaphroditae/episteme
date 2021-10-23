import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\ATSDDesk\Desktop\testdata1.xml')
root = tree.getroot()
#Print line tags for each page
def printlines():
    for i in range(6):
        if i > 0:
            print("          <line number = " + str(i) + "></line>") 
#Print page tags for book, print title
def printpages():
    print("<BarbersCornerExample>")
    for i in range(6):
        if i > 0:
            print( "<page number = ")
            printlines()
            print("     </page>")
    print("</BarbersCornerExample>")
    return
#Iterate over all ElementTree for search term
def search():
    target = input("Enter a name: ")
    for child in root:
        if target in child.text:
            print(child.tag, child.attrib)

#Main xml setup
def xmlsetup():
    printpages()

#Main menu func
def main():
    user = input("Enter the number corresponding to that option to run command: \n1. Run XML file setup.\n2. Search for term: ")
    if user == "1":
       xmlsetup()
    if user == "2":
        search()
            

main()
