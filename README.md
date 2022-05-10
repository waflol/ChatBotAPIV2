
# ChatterBot

ChatterBot là một công cụ hội thoại dựa trên máy học được xây dựng bằng Python, 
giúp tạo phản hồi dựa trên bộ sưu tập các cuộc hội thoại đã biết. 
Thiết kế độc lập với ngôn ngữ của ChatterBot cho phép nó được đào tạo để nói bất kỳ ngôn ngữ nào.

[![Package Version](https://img.shields.io/pypi/v/chatterbot.svg)](https://pypi.python.org/pypi/chatterbot/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Django 2.0](https://img.shields.io/badge/Django-2.0-blue.svg)](https://docs.djangoproject.com/en/2.1/releases/2.0/)
[![Build Status](https://travis-ci.org/gunthercox/ChatterBot.svg?branch=master)](https://travis-ci.org/gunthercox/ChatterBot)
[![Documentation Status](https://readthedocs.org/projects/chatterbot/badge/?version=stable)](http://chatterbot.readthedocs.io/en/stable/?badge=stable)
[![Coverage Status](https://img.shields.io/coveralls/gunthercox/ChatterBot.svg)](https://coveralls.io/r/gunthercox/ChatterBot)
[![Code Climate](https://codeclimate.com/github/gunthercox/ChatterBot/badges/gpa.svg)](https://codeclimate.com/github/gunthercox/ChatterBot)
[![Join the chat at https://gitter.im/chatterbot/Lobby](https://badges.gitter.im/chatterbot/Lobby.svg)](https://gitter.im/chatterbot/Lobby?utm_source=badge&utm_medium=badge&utm_content=badge)

Ví dụ:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  

## Dependencies

Trước khi sử dụng vui lòng chạy hai dòng dưới trên terminal

```
pip install -r requirement.txt
pip install -r dev-requirement.txt
```
## Running
### For running on flask
- B1: Chạy app.py
- B2: Để chat với bot thì theo đường dẫn http://192.168.1.79:5000/chat hoặc http://127.0.0.1:5000/chat với việc gửi theo phương thức POST và arg dict với key là req (Có thể sử dụng postman kiêm tra). 
Ví dụ:
![alt text](https://github.com/waflol/ChatBotAPIV2/blob/main/graphics/PostmanTestchat.png)
- B3: Để dạy bot thì theo đường dẫn http://192.168.1.79:5000/teach hoặc http://127.0.0.1:5000/teach với việc gửi theo phương thức POST và arg dict với 2 key là input và output (Có thể sử dụng postman kiêm tra). Sau train xong bên API sẽ trả về{"res_teach": "Done!"}
![alt text](https://github.com/waflol/ChatBotAPIV2/blob/main/graphics/PostmanTestteach.png)
### For running on terminal
- B1: Qua file main.py
- B2: MỞ comment trong đoạn DEMO và END DEMO
- B3: Chat bình thường thì chỉ cần comment lại đoạn code ở dưới
```
# Teach by user
statements = ["What's up?", "How are you?"]
User_teach(bot,statements)
```
- B4: Sau đó chạy file main.py
- B5 (optional): Để dạy bot thì mở phần comment ở dưới. Trong statements ta sẽ thêm 2 chuỗi input và output mong muốn theo dạng [input,output]
```
# Teach by user
statements = ["What's up?", "How are you?"] # [input,output]
User_teach(bot,statements)
```
## Basic Usage

```
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
```

# Training data
ChatterBot đi kèm với một mô-đun tiện ích dữ liệu có thể được sử dụng để đào tạo các bot trò chuyện. 
Hiện tại, có dữ liệu đào tạo cho hơn một chục ngôn ngữ trong mô-đun này. 
Những đóng góp về dữ liệu đào tạo bổ sung hoặc dữ liệu đào tạo bằng các ngôn ngữ khác sẽ được đánh giá rất cao. 
Hãy xem các tệp dữ liệu trong gói [chatterbot-corpus](https://github.com/gunthercox/chatterbot-corpus)

```
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
```



# [Documentation](https://chatterbot.readthedocs.io/)

Xem tài liệu chi tiết của chatterbot tại [đây](https://chatterbot.readthedocs.io/)

# Reference

See release notes for changes https://github.com/gunthercox/ChatterBot/releases
