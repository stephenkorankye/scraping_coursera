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
        # sections = soup.find( "div" , class_="offerings-wrapper").find_all( "div" , class_="rc-CardSection productCard-titleSection")
        sections = soup.find( "div" , class_="offerings-wrapper").find_all( "div" , class_="rc-CardSection productCard-titleSection")
        # print (  ( sections))

        for section in sections : 
            print ( section ) 
            # link = soup.find( "a").get_text() 
            # print ( link ) 
            print ('\n')
            
        print ( len ( sections ))


    funct() 

    


except Exception as e :
    print ( e ) 
