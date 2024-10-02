from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Настройки электронной почты
EMAIL_ADDRESS = 'vadekqwe@gmail.com'  # Ваш email
EMAIL_PASSWORD = 'zdcg samw vffe psxb'

def send_email(email, question,):
    # Настройка сообщения
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = 'ТЕ ОПЯТЬ МАМОНТ НАПИСАЛ'

    body = f'Email: {email}\nвопрос: {question}'
    msg.attach(MIMEText(body, 'plain'))

    # Отправка письма
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        email = request.form['email']
        question = request.form['question']


        # Отправка email
        send_email(email, question,)


        return redirect(url_for('success'))
    return render_template('index.html')


@app.route('/success')
def success():
    return 'Форма успешно отправлена!'


if __name__ == '__main__':
    app.run(debug=True)