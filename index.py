from bs4 import BeautifulSoup 
import requests , openpyxl 



query = "Machine Learning" 
query = "%20".join(query.split(" "))


def single_course(url) : 
    source = requests.get (url) 

    source.raise_for_status() 

    soup = BeautifulSoup(source.text , "html.parser")
    main = soup.find("main").find("div" , class_="rc-BannerInstructorInfo")
    main = main.find("a").get_text(strip=True)

    print ( main ) 


    

# url = "https://www.coursera.org/specializations/statistics"
# url = "https://www.coursera.org/learn/marketing-analytics-foundation"
url = "https://www.coursera.org/professional-certificates/ibm-data-science"

single_course(url) 


'''
try : 

    def funct() :

        # url = "https://www.coursera.org/search?query=" + query
        url = "https://www.coursera.org/browse/data-science"
        print ( url )
        source = requests.get (url) 

        source.raise_for_status() 

        soup = BeautifulSoup(source.text , "html.parser")
        
        sections = soup.find( "div" , class_="offerings-wrapper").find_all( "div" , class_="rc-CardSection productCard-titleSection")


        for section in sections : 

            # Getting the Links for each course 
            link = section.find("div").find("a")
            href = link.get("href")
            print ( href ) 

            print ('\n')
            
        print ( len ( sections ))


    funct() 

    


except Exception as e :
    print ( e ) 

'''