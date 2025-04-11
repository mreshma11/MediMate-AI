import smtplib

from email.message import EmailMessage

from twilio.rest import Client



# --- Mailtrap Email Alert ---

def send_email_alert(message_body, to_email="# mobile_number@sms_gateway_domain"):

    msg = EmailMessage()

    msg.set_content(message_body)

    msg["Subject"] = "MediMate AI Alert"

    msg["From"] = "demo@temporarymail.com"

    msg["To"] = to_email



    smtp_server = "smtp.mailtrap.io"

    smtp_port = 587

    smtp_user = "c4b6f96a947bec"

    smtp_pass = "83b06ed5fe8f5b"



    with smtplib.SMTP(smtp_server, smtp_port) as smtp:

        smtp.starttls()

        smtp.login(smtp_user, smtp_pass)

        smtp.send_message(msg)

        print(f"[📩 Mailtrap Email Sent] to {to_email}")





# --- Twilio Real SMS Alert ---

def send_sms_alert_real(phone_number="# mobile_number", message_body="Emergency detected. Please check immediately."):

    account_sid = "ACe94dc6f97e937843cc385fe9bdc92eec"

    auth_token = "34250146dd9964f2f8ce6fb4b2f30c9e" #twilio account for hosting own sms server

    twilio_number = "+18126083540"



    client = Client(account_sid, auth_token)

    message = client.messages.create(

        body=message_body,

        from_=twilio_number,

        to=phone_number

    )

    print(f"[📲 Real SMS Sent] to {phone_number}")





# --- Combined Alert Function ---

def send_combined_alert(message_body="🚨 Emergency: High BP and No Movement detected."):

    print("[🚨] Triggering both Email and SMS Alerts...\n")

    send_email_alert(message_body)

    send_sms_alert_real(message_body=message_body)
