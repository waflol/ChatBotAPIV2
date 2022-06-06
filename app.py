from chatterbot import ChatBot
from flask import Flask,request,jsonify
from chatterbot.filters import get_recent_repeated_responses
from main import initialize_Corpus,User_teach,get_response, initialize_CorpusDetail
import sys,os

isMainTraining = False
if os.path.exists('./database.sqlite3') == False:
    isMainTraining = True

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

app = Flask(__name__)
if isMainTraining:
    initialize_Corpus(bot)
    
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


@app.route("/newBot",methods=['POST'])
def newBot():
    user_id = request.get_json()["user_id"]
    language = request.get_json()["language"]
    db_url = 'sqlite:///database_'+user_id+'_'+language+'.sqlite3'
    user_bot = ChatBot(
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
                        database_uri=db_url
                    )
    initialize_CorpusDetail(user_bot,lang=language)
    return jsonify(res='Done initialization!',ResUser_id=user_id)

@app.route("/chatuserbot",methods=['POST'])
def chatUserBot():
    Input = request.get_json()["req"]
    user_id = request.get_json()["user_id"]
    language = request.get_json()["language"]
    db_url = 'sqlite:///database_'+user_id+'_'+language+'.sqlite3'
    if os.path.exists('./'+db_url.split("///")[-1]):
        user_bot = ChatBot(
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
                        database_uri=db_url
                    )
        Output = get_response(user_bot,Input)
        return jsonify(res=Output.text)
    else:
        return jsonify(res="Error!")
    
@app.route("/teachuserbot",methods=['POST'])
def teachUserBot():
    input_s = request.get_json()["input"]
    output_s = request.get_json()["output"]
    statements = [input_s,output_s]
    user_id = request.get_json()["user_id"]
    language = request.get_json()["language"]
    db_url = 'sqlite:///database_'+user_id+'_'+language+'.sqlite3'
    user_bot = ChatBot(
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
                    database_uri=db_url
                )
    return jsonify(res_teach=User_teach(user_bot,statements))

@app.route("/deleteduserbot",methods=['POST'])
def deleteUserbot():
    user_id = request.get_json()["user_id"]
    language = request.get_json()["language"]
    db_url = 'sqlite:///database_'+user_id+'_'+language+'.sqlite3'
    path_file = './'+db_url.split('///')[-1]
    if os.path.exists(path_file):
        os.remove(path_file)
    return jsonify(res_delete="Done!")

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=os.environ.get('DEBUG')=='1',port=int(os.environ.get("PORT", 8080)))
    
    
# docker run -p 5000:5000 -e DEBUG=1 <image-name>

