"""
Identifiers:
^ Start of a string
$ End of a string
\. Anycharacter or characters except \n eg .art returns art, fart, hart, cart
* Match one character preceding 0+ times '.c*' cat, cart, chart
& Stop, matches at end of string $.art at end of string 
+ match one character 1+ times
^matches characters if they are at the start of the string, ^.art if at beg of string
? matches 0 or 1 char Non-greedy
\s Whitespace
\S Non-whitespace
\w word character
\W not a word character
() contains sup-expressions
\t tab, \f form feed, \r return, \e escape
\d any number(digit)
\D anything but a number

\b anywhitespace around words #word boundary
\B not a word boundary
\. a period
| either or
{}  range or single value

[abc] Match one character in the specified set, or single chars
[^abc] Match one character NOT in the specied set
[0-9]+ pulls out all numbers
[^] not in set

Meta characters that need to be escaped with \
    .[{()\^$|?*+


match() sees if string is at begining
search() sees if there is a match within the string

"""



import re

string = "Here is an email pantscranky@gmail.com that has 785 98990 3 spam messages."
result = re.findall('[0-9]+', string)
print(result)

result = re.findall('[^a-z]+', string)
print(result)

#extracting email
result = re.findall('\S+@\S+', string)
print(result)

def main():
    string = "this is a string for regular expressions"
    match_result = re.match('regular', string, re.M|re.I)
    if match_result:
        print("Match was found: " + match_result.group())
    else:
        print("No match found.") 

    search_result = re.search('regular', string, re.M|re.I)
    if search_result:
        print("Match was found: " + search_result.group())
    else:
        print("No match found.")  

main()  


ages = [5,16,35,29]
names = ["Charlie", "Benny", "Joon", "Oscar"]
diction = {}
i=0
for name in names:
    diction[name] = ages[i]
    i += 1
print(diction)  

string = """444-453-7786 444.352.6711 444%673^3333 asf ASDF asdfAFRR cat hat bat mat
Mr. Murray Ms Mary Mrs. Taylor Mrs. Campion Mr Starr Mr. K
emailaddress@gmail.com EmailADress@gmail.com EmailAdDress@gmail.com
email.address@gmail.edu email-address990@gmail.com"""
url_list = """https://www.google.com http://website.com https://youtube.com https://nasa.gov"""
number = re.findall('\d\d\d.\d\d\d.\d\d\d\d',string)
number2 = re.findall('\d\d\d[-.]\d\d\d[-.]\d\d\d\d', string) 
letter = re.findall('[a-zA_Z]',string) 
letter2 = re.findall('[a-z]',string)  
setf = re.findall('[^a|A]',string)  
at = re.findall("[^b]at",string)
number3 = re.findall('\d{3}.\d{3}.\d{4}', string)
mrs = re.findall('Mr\.?\s[A-Z]\w*',string)
mrss = re.findall('M(r|s|rs)\.?\s[A-Z]\w*',string)
email = re.findall('[a-zA-Z]+@[a-zA-Z]+\.com',string)
emails = re.findall('[a-zA-Z.]+@[a-zA-Z]+\.com',string)  
email2 =  re.findall('[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)',string)  
email3 =  re.findall("[a-zA-Z.0-9-]+@[a-zA-Z0-9-]+\.(com|edu)+",string)      
email4 =  re.findall("[a-zA-Z_.0-9-+]+@[a-zA-Z0-9-]+\.[a-zA-Z.0-9-]+",string)
websites = re.findall('https?://[(www\.)]?\w+\.\w+', url_list)

print(number, number2)
print(letter,letter2)
print(setf)
print(at)
print(number3)
print(mrs)
print(mrss)
print(email,emails,email2,email3,email4)
print(websites)

