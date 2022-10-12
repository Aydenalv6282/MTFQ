import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("havenraffaello@gmail.com", "uzfesqwkwdhxnozz")

# message to be sent
text = "Title Here"
subject = "Text Here"
message = ('Subject:{}\n\n'+text).format(subject)

# sending the mail
for i in range(999):
    mid = "%03d" % i
    number = "305"+mid+"8349"
    print(number)
    #s.sendmail("havenraffaello@gmail.com", number+"@tmomail.net", message, )
# terminating the session
s.quit()
print("done")
