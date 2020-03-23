

def mail(SERVER, sender, to, subject, message):
    server = smtplib.SMTP(SERVER)
    #server.set_debuglevel(1)
    server.ehlo()
    server.sendmail(sender, to, message)
    server.quit()


# To call

mail(SERVER, 'email@google.com'
    ['myemail@google.com']
    'This is a subject', msg_body)




