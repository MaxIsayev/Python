import smtplib, ssl
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#define email addresses and password
sender_email = "MaxTestPython@mail.ru"
receiver_email = "MaxTestPython@mail.ru"
password = 'Post3640313!'
#define message properties
message = MIMEMultipart("alternative")
message["Subject"] = "Test app"
message["From"] = sender_email
message["To"] = receiver_email
#define text for plain email format
text = """\
This is python test program written by Maxim Isayev"""
#begin construct html mail
html1 = """\
<html>
<head>
 <title>Aircraft information</title>
</head>
<body>
<table>"""
#connect to database
conn = sqlite3.connect('D:\Programming_task\Database2.db')
#1st table columns headers
htmlHead = """<tr bgcolor="#ADD8E6"><th>TAIL_NUMBER</th><th>MODEL_NUMBER</th><th>MODEL_DESCRIPTION</th><th>OWNER_COMPANY_NAME</th><th>COMPANY_COUNTRY_CODE</th><th>COMPANY_COUNTRY_NAME</th></tr>"""
htmlrow = ""
#1st table data 
cursor = conn.execute('SELECT TAIL_NUMBER, MODEL_NUMBER, DESCRIPTION, COMPANY_NAME, COUNTRY_CODES.CODE, COUNTRY_CODES.COUNTRY_NAME,' 
+' COUNTRY_CODES.SDF_COC_003'  
+' FROM AIRCRAFT' 
+' INNER JOIN MODEL ON AIRCRAFT.MDL_AUTO_KEY = MODEL.MDL_AUTO_KEY'
+' INNER JOIN COMPANIES ON AIRCRAFT.CMP_OWNER = COMPANIES.CMP_AUTO_KEY'
+' INNER JOIN COUNTRY_CODES ON COUNTRY_CODES.COC_AUTO_KEY = COMPANIES.COC_AUTO_KEY'
+" WHERE SDF_COC_003 = 'T'"
+' ORDER BY COUNTRY_CODES.COUNTRY_NAME')
for row in cursor:
    htmlrow = htmlrow+"<tr bgcolor=""#ADD8E6""><th>"+row[0]+"</th><th>"+row[1]+"</th><th>"+row[2]+"</th><th>"+row[3]+"</th><th>"+row[4]+"</th><th>"+row[5]+"</th></tr>"
#1st table is constructed using 3 variable and some html text
html= html1 + htmlHead + htmlrow +'</table><br>'
#2nd table headers
htmlHead = """<table><tr bgcolor="#FA8072"><th>TAIL_NUMBER</th><th>MODEL_NUMBER</th><th>MODEL_DESCRIPTION</th><th>OWNER_COMPANY_NAME</th><th>COMPANY_COUNTRY_CODE</th><th>COMPANY_COUNTRY_NAME</th></tr>"""
#2nd table data
cursor = conn.execute('SELECT TAIL_NUMBER, MODEL_NUMBER, DESCRIPTION, COMPANY_NAME, COUNTRY_CODES.CODE, COUNTRY_CODES.COUNTRY_NAME,' 
+' COUNTRY_CODES.SDF_COC_003'  
+' FROM AIRCRAFT' 
+' INNER JOIN MODEL ON AIRCRAFT.MDL_AUTO_KEY = MODEL.MDL_AUTO_KEY'
+' INNER JOIN COMPANIES ON AIRCRAFT.CMP_OWNER = COMPANIES.CMP_AUTO_KEY'
+' INNER JOIN COUNTRY_CODES ON COUNTRY_CODES.COC_AUTO_KEY = COMPANIES.COC_AUTO_KEY'
+" WHERE SDF_COC_003 = 'F'"
+' ORDER BY COUNTRY_CODES.COUNTRY_NAME')
htmlrow = ""
for row in cursor:
    htmlrow = htmlrow+"<tr bgcolor=""#FA8072""><th>"+row[0]+"</th><th>"+row[1]+"</th><th>"+row[2]+"</th><th>"+row[3]+"</th><th>"+row[4]+"</th><th>"+row[5]+"</th></tr>"
#2nd table is constructed and attached to html
html= html + htmlHead + htmlrow +'</table>'
#html document ending
html2 = """\
</table>
</body></html>"""

html= html + html2
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.mail.ru",465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Program finished operation')