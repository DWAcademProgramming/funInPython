import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "welshdavmsu@gmail.com"
    password = "----"
    receiver = "welshdavmsu@gmail.com"
    context = ssl.create_default_context()
    message = """
Does this fucking work? 
"""
    with smtplib.SMTP_PORT(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()