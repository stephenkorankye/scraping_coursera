from bs4 import BeautifulSoup 
import requests , openpyxl 



query = "Machine Learning" 
query = "%20".join(query.split(" "))

try : 

    def funct() :

        # url = "https://www.coursera.org/search?query=" + query
        url = "https://www.coursera.org/browse/data-science"
        print ( url )
        source = requests.get (url) 

        source.raise_for_status() 

        soup = BeautifulSoup(source.text , "html.parser")
        
        # print ( soup ) 
        courses = soup.find( "section" , class_="rc-ProductOfferings").find_all("section")
        print (  len( courses))


    funct() 

    


except Exception as e :
    print ( e ) 
