import smtplib
from email.message import EmailMessage
import subprocess


def is_locked() -> bool:
    result = subprocess.check_output("TASKLIST")
    return b"LogonUI.exe" in result


def send_alert() -> None:
    msg = EmailMessage()
    msg["From"] = "robot@friend.dk"
    msg["To"] = ["ghbm@aarhus.dk", "kriba@aarhus.dk"]
    msg["Subject"] = "Læseskærm er aktiv!"
    msg.set_content(
        "Hjælp læseskærmen er aktiv!"
    )

    with smtplib.SMTP("smtp.adm.aarhuskommune.dk", 25) as smtp:
        smtp.starttls()
        smtp.send_message(msg)


if __name__ == "__main__":
    if is_locked():
        send_alert()