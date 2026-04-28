
from email.message import EmailMessage
import smtplib
from datetime import datetime

import pyodbc


SQL = """
SELECT process_status, next_run
  FROM [Scheduled_Triggers] as a
  JOIN [Triggers] as b ON a.id = b.id
"""


def count_late_triggers():
    connection = pyodbc.connect("Server=SRVSQLHOTEL04;Database=MKB-ITK-RPA;Trusted_Connection=yes;Driver={ODBC Driver 17 for SQL Server}")
    result = connection.execute(SQL)

    count = 0

    for status, next_run in result:
        if status == "IDLE" and next_run < datetime.now():
            count += 1

    return count


def send_alert(count: int) -> None:
    msg = EmailMessage()
    msg["From"] = "robot@friend.dk"
    msg["To"] = ["ghbm@aarhus.dk", "kriba@aarhus.dk"]
    msg["Subject"] = "Robotter er ikke gået i gang til tiden!"
    msg.set_content(
        f"Hjælp! {count} robotter er ikke gået i gang til tiden!! 😨"
    )

    with smtplib.SMTP("smtp.adm.aarhuskommune.dk", 25) as smtp:
        smtp.starttls()
        smtp.send_message(msg)


if __name__ == '__main__':
    count = count_late_triggers()
    if count > 2:
        send_alert(count)