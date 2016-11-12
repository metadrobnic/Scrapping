from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup

base_url = "https://scrapebook22.appspot.com/" #to mamo zdej url ki ga bomo importal

response = urlopen(base_url).read()  #s tem odpremo ta url in dobimo njegove podatke

#zdaj bomo s parsanjem dobili podatke ven z BeautifulSoup


soup = BeautifulSoup(response)


seznam_emailov = []

podatki = []

print(soup.html.head.title.string)  #to bomo dobil ven title spletne strani

for link in soup.findAll("a"):  #po vsem htmlju bo iskal a-je (a href) in nam jih izpisal
   if link.string == "See full profile":
        person_url = base_url + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        ime_priimek = person_soup.find("div", attrs={"class": "row"}).h1.string
        email = person_soup.find("span", attrs={"class": "email"})
        city = person_soup.find("span", attrs={"data-city": True})
        seznam_emailov.append(str(email.string))
        podatki.append((ime_priimek, str(email.string), str(city.string)))

       # print(email.string)
print(podatki)


emails = open("emails.txt", "w") #pisemo v datoteko

for email in seznam_emailov:
    emails.write(email + ";\n")

emails.close()

#create CVS file

cvs_file = open("emails.cvs", "w")

for p in podatki:
    cvs_file.write(p[0] + ", " + p[1] + ", " + p[2] +"\n")

cvs_file.close()







"""
with open("emails.txt", "w") as emails:   To das lahko namesto emails.close() oz zgornjih stirih vrstic
    for email in seznam_emailov:
      emails.write(email + ";\n")
 """

