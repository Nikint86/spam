import smtplib
import os
my_secret = os.environ['PASSWORD']
login = "Nik.Lobatskiy@yandex.by"
otg = "Nik.Lobatskiy@yandex.by"
sender_name = "Nik.Lobatskiy@yandex.by"
email_k = "Nik.Lobatskiy@yandex.by"
k = "Diana@yandex.by"
sub = "Приглашение!"
сoc = 'Content-Type: text/plain; charset="UTF-8"'
letter = """From: {0} 
To: {1} 
Subject: {2} 
{3}
""".format (otg,k,sub,сoc)
text= """\nПривет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
text = text.replace("%website%","https://dvmn.org/referrals/i90Pn3DpMXqGmpKob3JQ8rd1BqrJhfw3bJV83ZsE/")
text = text.replace("%friend_name%","Вася")
text = text.replace("%my_name%","Никита")
text = text.encode("UTF-8")
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, my_secret)
server.sendmail(sender_name,email_k, letter+text)
server.quit()












