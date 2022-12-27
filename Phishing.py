import smtplib
import validators
from urllib import request
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def creatmail(Username, mail, title, jod_title , personal_status, kid1, kid2, kid3, kid4,text_info):
    text = f"hello {title} {text_info.get('name')} \n\n"

    text += f"we get your details from {text_info['sender title']} {text_info['sender']} \n"

    text += f"hi think that this will be relevant for you \n\n"

    if title == "prof." or title == "dr.":
        text += "ariel universty wonted to update you about a new research that we made in our university:\n"
        if kid1 == "no":
            if personal_status == "merid":
                 text += "the research is about merid pepole and there relushionship\n "
            if personal_status == "devors":
                 text += "the research is about devors pepole and struggels\n "
            if personal_status == "singel":
                 text += "the research is about singel pepole and struggels \n "
        else:
            if 0<kid1<=5 or 0<kid2<=5 or 0<kid3<=5 or 0<kid4<=5:
                text += "the research is about kids in ages betweean 0 to 5\n "
            elif 5<kid1<=10 or 5<kid2<=10 or 5<kid3<=10 or 5<kid4<=10:
                text += "the research is about kids in ages betweean 0 to 5\n "
            elif 10<kid1<=18 or 10<kid2<=18 or 10<kid3<=18 or 10<kid4<=18:
                text += "the research is about kids in ages betweean 0 to 5\n "
        
        text+="your opinion is very importent to as and we would like you to read the research and give your opinion in this \n thank you for your time \n "
    else:
        text += "SuperCheap is wanted to update you about the new branch that we opening in your city:\n we have the best price in the market \n and we have lot of new sale for our opening like \n"
        if kid1 == "no":
            if jod_title == "trainer":
                 text += "5 kg og way protin in 200 sheckels\n full body training machine in only 1500 sheckels \n and lots of other sales \n"
            if jod_title == "developer":
                 text += "dell entrprais 4999 computer with i9 prosseore and 32 rm and 512 ssd in only 4000 sheckels\n mouse and keybourd only in 99.00 sheckels \n and lots of other sales \n "
            if jod_title == "plamer":
                 text += "pipe wrench in only 99.90 sheckels\n full tool box with all you need in  399.00 sheckels \n and lots of other sales"
        else:
            if 0<kid1<5 or 0<kid2<5 or 0<kid3<5 or 0<kid4<5:
                text += "5 packets of pampers dipers in 199.90 sheckels\n 5 packet of wipes in only 29.90 sheckels \n and lots of other sales"
            elif 5<kid1<10 or 5<kid2<10 or 5<kid3<10 or 5<kid4<10:
                text += "bike of kids for only 399.90 sheckels\n backpack for only 99.90 sheckels \n  and lots of other sales"
            elif 10<kid1<18 or 10<kid2<18 or 10<kid3<18 or 10<kid4<18:
                text += "playstation 5 in  1999.90 sheckels\n aripods in only 499.00 sheckels \n and lots of other sales"
            text+= "for more informashion about our sales and for our laction visit as in our website \n we will be happy to see you there"
    return text

def get_mail_info(sorece):
    valid=validators.url('gist.github.com/dperini/729294')
    print(valid)
    if valid==True:
        print("Url is valid")
        response = request.urlretrieve(sorece, "mytext.txt")
        sorece = "mytext.txt"
    else:
        print("Invalid url")
    
    try:
        filename = sorece
        with open(filename, 'r') as file:
            sorece = file.read().replace('\n', ' ')
    except:
        print("notext")
    split_text = sorece.split(' ')
    file_info = {}
    file_info['name'] = split_text[2]
    file_info['sender'] = split_text [-1]
    file_info['sender title'] = split_text [-2]
    return file_info
    
myarges = sys.argv
fromaddr = "*********@gmail.com" # needs an email
toaddr = myarges[2]

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "you have to see this"
if len(myarges) == 11:
    sorece = myarges[10]
else:
    sorece = "mytext.txt"
mail_info = get_mail_info(sorece)

body = creatmail(myarges[1], myarges[2], myarges[3], myarges[4] , myarges[5], int(myarges[6]), int(myarges[7]), int(myarges[8]), int(myarges[9]),mail_info)

msg.attach(MIMEText(body, 'plain'))

filename = "attachment.py"
attachment = open("attachment.py", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "************") # needs token
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()