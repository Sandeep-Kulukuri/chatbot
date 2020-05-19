#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
from chatterbot import corpus
app = Flask(__name__)
bot = ChatBot("Candice")
trainer = ListTrainer(bot)
path =  r'C:\Users\sande\PycharmProjects\chatbot\chatbot_datasets'
for _file in os.listdir(path):
    with open(os.path.join(path,_file),'r',encoding='utf8') as f:
        chats = f.readlines()
        trainer.train(chats)


#trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()