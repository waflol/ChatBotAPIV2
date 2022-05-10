from chatterbot import ChatBot
from flask import Flask,request,jsonify
from chatterbot.filters import get_recent_repeated_responses
from main import initialize_Corpus,User_teach,get_response

bot = ChatBot(
    'Example Bot',
    filters=[get_recent_repeated_responses],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. Please teach me!',
            'maximum_similarity_threshold': 0.95
        },
    ],
    database_uri='sqlite:///database.sqlite3'
)
initialize_Corpus(bot)
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/teach",methods=['POST'])
def teach():
    input_s = request.get_json()["input"]
    output_s = request.get_json()["output"]
    statements = [input_s,output_s]
    return jsonify(res_teach=User_teach(bot,statements))

@app.route('/chat',methods=['POST'])
def chatBot():
    Input = request.get_json()["req"]
    Output = get_response(bot,Input)
    return jsonify(res=Output.text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)

