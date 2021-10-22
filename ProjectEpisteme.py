from typing import Text
import xml.etree.ElementTree as ET
tree = ET.parse(r'S:\Tori\Episteme.xml')
root = tree.getroot()

def printvalue():
    print("              <value></value>")

#Print line tags for each page
def printlines():
    for i in range(6):
        if i > 0:
            print("          <line" + str(i) + "></line" + str(i) + ">") 

#Print page tags for book, print title
def printpages():
    print("<BarbersCornerExample>")
    for i in range(6):
        if i > 0:
            print("     <page" + str(i) + ">")
            printlines()
            print("     </page" + str(i) + ">")
    print("</BarbersCornerExample>")
    return

#Create search functionality within the xml file
def menu():
    name = input("Search for a name: ")

#Iterate over all ElementTree for search term
def search():
    pass

#main xml setup
def xmlsetup():
    printpages()


def main():
    user = input("Enter the number corresponding to that option to run command: \n1. Run XML file setup.\n2. Search for term: ")
    if user == "1":
       xmlsetup()
    if user == "2":
        search()

def search():
    x = 0
    target = input("Input the name you would like to search: ")
    for child in root:
        print(child.tag)
            

#for idx, val in enumerate(root[0]):
    #print(idx, val, Text)

#root.findall(".=['Tori']")
#print(search)
#root[0].attrib


target = input("Enter a name you would like to search: \n")

found = [element for element in root.iter() if element.text == target]
print(found)