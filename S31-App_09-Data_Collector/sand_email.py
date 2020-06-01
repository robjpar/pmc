from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count, simulate=True):
    from_email = 'my_email@gmail.com'
    # from_password = 'my_password'
    to_email = email
    subject = 'Height data'
    message = 'Hey there, your height is <strong>{}</strong> cm.<br>Average height of all \
is <strong>{}</strong> cm and that is calculated out of <strong>{}</strong> people.\
<br>Thanks!'.format(height, average_height, count)
    
    if simulate:
        print(message)
    else:
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['To'] = to_email
        msg['From'] = from_email

        # s = smtplib.SMTP('smtp.gmail.com', 587)
        s = smtplib.SMTP('localhost', 1025)
        # s.ehlo()
        # s.starttls()
        # s.login(from_email, from_password)
        s.send_message(msg)
        s.quit()
