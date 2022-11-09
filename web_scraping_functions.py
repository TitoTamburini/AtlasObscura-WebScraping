from bs4 import BeautifulSoup
import os
from datetime import datetime
import linecache
#Create ordered by page directories for tsv files
def create_tsv_directories():
    for page_index  in range(1,401):
        dir_path  = "TSV_FILES/page"+str(page_index)
        if not os.path.exists(dir_path):
                os.makedirs(dir_path)
#All web-scraping functions to scrape desired data for each Place on Atlas-Obscura.com

def get_placeTags(soup):
    return  [x.text.replace('\n',"") for x in soup.find_all('a',{'class' : 'itemTags__link' })]

def get_placeName(soup):
    return  soup.find('h1',{'class' : 'DDPage__header-title' }).text.strip()

def get_placePeopleVisited(soup):
    first_div = soup.find('div',{'class': 'col-xs-4X js-submit-wrap js-been-to-top-wrap action-btn-col hidden-print'})
    return first_div.find('div',{'class': 'title-md item-action-count'}).text

def get_placePeopleWant(soup):
    first_div = soup.find('div',{'class': 'col-xs-4X js-submit-wrap js-like-top-wrap action-btn-col hidden-print'})
    return first_div.find('div',{'class': 'title-md item-action-count'}).text

def get_placeDesc(soup):
    placeDesc = [x.text.replace("\xa0"," ") for x in soup.find('div',{'id': 'place-body'}).findChildren('p')]
    return ''.join(placeDesc)

def get_placeShortDesc(soup):
    return   soup.find('h3',{'class' :'DDPage__header-dek'}).text.strip()

def get_placeNearby(soup):
    return [x.text for x in soup.find_all('div',{'class':'DDPageSiderailRecirc__item-title'})]

def get_placeAddress(soup):
    address_tag =  soup.find('address',{'class':'DDPageSiderail__address'})
    div = address_tag.find('div')
    address =""
    if(len(div.contents) > 4):
        address = div.contents[0]+", "+div.contents[2]+", "+div.contents[4]
    return address

def get_placeCoordinates(soup):
    coord_div  = soup.find('div',{'class':'DDPageSiderail__coordinates js-copy-coordinates'})
    coord = coord_div.get('data-coordinates').split(',')
    placeAlt,placeLong = list(map(float,coord))
    return placeAlt,placeLong

def get_placeEditors(soup):
    editors_list = []
    soup_obj  = soup.findAll('li',{'class':'DDPContributorsList__item'})
    for li in soup_obj:
        editors_list.append(li.find('span').text)
    return editors_list

def get_placePubDate(soup):
    return datetime.strptime(soup.find('div',{'class':'DDPContributor__name'}).text,'%B %d, %Y').date()

def get_placeRelatedLists(soup):
   div = soup.findAll('div',{'class':'card-grid CardRecircSection__card-grid js-inject-gtm-data-in-child-links'})
   if(len(div)>2):
      return [x.find('span').text for x in div[2].findAll('a')]
   else:
      return ""

def get_placeRelatedPlaces(soup):
   div = soup.findAll('div',{'class':'card-grid CardRecircSection__card-grid js-inject-gtm-data-in-child-links'})
   if(len(div)>1):
      return [x.find('span').text for x in div[1].findAll('a')]
   else:
      return ""

def make_place_tsv(place_number,tsv_path,html_path,url):
    if not os.path.exists(tsv_path+"/place_"+str(place_number)+'.tsv'): 
        try:
            with open(html_path,"r",encoding='utf-8') as html:
                soup = BeautifulSoup(html,'lxml')
                row = ""
                row += str(get_placeName(soup))+' \t'
                row += str(get_placeTags(soup))+' \t'
                row += str(get_placePeopleVisited(soup))+' \t'
                row += str(get_placePeopleWant(soup))+' \t'
                row += ' '+str(get_placeDesc(soup))+' \t'
                row += ' '+str(get_placeShortDesc(soup))+' \t'
                row+=' '+str(get_placeNearby(soup))+' \t'
                row+=' '+str(get_placeAddress(soup))+' \t'
                placeAlt,placeLong = get_placeCoordinates(soup)
                row +=' '+str(placeAlt)+' \t'
                row +=' '+str(placeLong)+' \t'
                row +=' '+str(get_placeEditors(soup))+' \t'
                row +=' '+str(get_placePubDate(soup))+' \t'
                row +=' '+str(get_placeRelatedLists(soup))+' \t'
                row+=' '+str(get_placeRelatedPlaces(soup))+' \t'
                row += ' '+url+' \t'
                #print(row)
                try:
                        with open(tsv_path+"/place_"+str(place_number)+'.tsv','w',encoding='utf-8') as f:
                            f.write(row)
                            print("csv created!")
                except  Exception as e:
                    print("File not Created: "+e)
        except Exception as e:
            print("Error occurred: "+str(e))
