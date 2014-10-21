from email.MIMEText import MIMEText
message="""Hello, This is a test message
                -- Anoynymous"""

msg=MIMEText(message)
msg['To']='recipient@example.com'
msg['From']='Test Sender <sender@example.com>'
msg['Subject']='Test Message'

print msg.as_string()
