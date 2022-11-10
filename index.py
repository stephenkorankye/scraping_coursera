from bs4 import BeautifulSoup 
import requests , openpyxl 



categories = {
    "Data Science" : "data-science" , 
    "Business": "business" , 
    "Computer Science" : "computer-science" , 
    "Personal Development" : "personal-development" , 
    "Language Learning": "language-learning", 
    "Information Technology" : "information-technology", 
    "Health": "health", 
    "Math and Logic": "math-and-logic", 
    "Physical Science Engineering" : "physical-science-and-engineering" , 
    "Social Sciences": "social-sciences", 
    "Arts and Humanities": "arts-and-humanites"

}




query = "Machine Learning" 
query = "%20".join(query.split(" "))


def single_course(base_url ,url) : 
    url = "https://coursera.org" + url 
    print ( url )
    source = requests.get (url) 

    source.raise_for_status() 

    soup = BeautifulSoup(source.text , "html.parser")
    main = soup.find("main") 

    instructor = main.find("div" , class_="rc-BannerInstructorInfo")
    instructor = instructor.find("a").get_text(strip=True).split("Â")[0]

    enrolled = soup.find("div" , class_="rc-ProductMetrics").find("strong").find("span").text or "N/A"

    course_name = soup.find("h1").text

    description = soup.find("div" , class_="description").find("div").text 
    
    ratings = main.find("div" , class_="XDPRating").find("div" , class_="color-white").find("span").find("span").text.split(" ")[0]

    # print ( instructor, enrolled , course_name , description , ratings )

    print ( enrolled )



    

url = "https://www.coursera.org/specializations/statistics"
# url = "https://www.coursera.org/learn/marketing-analytics-foundation"
# url = "https://www.coursera.org/professional-certificates/ibm-data-science"

# single_course(url) 



try : 

    def funct() :

        # url = "https://www.coursera.org/search?query=" + query
        url = "https://www.coursera.org/browse/" + categories["Health"]
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
            single_course( url , href )
            break 
             

           
            
        # print ( len ( sections ))


    funct() 

    


except Exception as e :
    print ( "There is an error")
    print ( e ) 
