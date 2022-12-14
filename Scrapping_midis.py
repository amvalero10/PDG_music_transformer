import requests
from bs4 import BeautifulSoup


pages = ['http://jsbach.blog68.fc2.com/blog-date-20130111.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130112.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130113.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130114.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130115.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130116.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130117.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130118.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130119.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130120.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130121.html',  
         'http://jsbach.blog68.fc2.com/blog-date-20130122.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130123.html',
         'http://jsbach.blog68.fc2.com/blog-date-20130124.html' ]

for j in pages:

    page = requests.get(j)
    #print(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())

    soup_all_a = soup.find_all('a')
    #print(soup_all_a)



    for i in soup_all_a:

        chars = "="
        check_string = str(i)
        cuentaEqu = 0

        for char in chars:
            count = check_string.count(char)
            if count > 1:
                cuentaEqu = count
                #print(char, count)


        if( str(i).__contains__('http://jsbach.blog68.fc2.com') 
            and str(i).__contains__('BWV') 
            and not str(i).__contains__('Next')
            and cuentaEqu >= 2
            ):

            print('----------------')
            print(i)

            page2 = requests.get(i['href'])
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            soup_all_a2 = soup2.find_all('a')
            #print(soup_all_a2)

            for k in soup_all_a2:
                if( str(k).__contains__('.mid') ):
                    print('>>>>>>>>>>>>>>')
                    print(k)

                    file = requests.get( k['href'] ).content 

                    nameArr = k['href'].split('/')
                    name = 'f'
                    for z in nameArr:
                        if str(z).__contains__('.mid'):
                            name = str(z)



                    with open(name, 'wb') as handler: 
                        handler.write(file) 






