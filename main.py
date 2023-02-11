from application.db.people import get_employees
from application.salary import calculate_salary
from  datetime import date
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

if __name__ == '__main__':
    print(f"Привет, сегодняшняя дата {date.today()}", end="\n\n")
    engine.say(f"Привет, сегодняшняя дата {date.today()}")
    get_employees()
    calculate_salary()
engine.runAndWait()