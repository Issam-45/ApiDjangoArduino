from django.db import models
import telepot, pywhatkit

token = "5907427756:AAF6IA7Y5fnFoS9rBFi51YuxP8l8gyT3U1s"
chat_id = "1911730761"
bot = telepot.Bot(token)

class Dht (models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 10:
            bot.sendMessage(chat_id, "High temp!" + str(self.temp))
            pywhatkit.sendwhatmsg_instantly(f"+212604009484", 'vvvv')
        return super().save(*args, **kwargs)
