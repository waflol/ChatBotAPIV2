![ChatterBot: Machine learning in Python](https://i.imgur.com/b3SCmGT.png)

# ChatterBot

ChatterBot là một công cụ hội thoại dựa trên máy học được xây dựng bằng Python, 
giúp tạo phản hồi dựa trên bộ sưu tập các cuộc hội thoại đã biết. 
Thiết kế độc lập với ngôn ngữ của ChatterBot cho phép nó được đào tạo để nói bất kỳ ngôn ngữ nào.

[![Package Version](https://img.shields.io/pypi/v/chatterbot.svg)](https://pypi.python.org/pypi/chatterbot/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Django 2.0](https://img.shields.io/badge/Django-2.0-blue.svg)](https://docs.djangoproject.com/en/2.1/releases/2.0/)
[![Requirements Status](https://requires.io/github/gunthercox/ChatterBot/requirements.svg?branch=master)](https://requires.io/github/gunthercox/ChatterBot/requirements/?branch=master)
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

## How it works

Một phiên bản chưa được đào tạo của ChatterBot bắt đầu mà không có kiến thức về cách giao tiếp. Mỗi khi người dùng nhập một câu lệnh, thư viện sẽ lưu văn bản mà họ đã nhập và văn bản mà câu lệnh đó được phản hồi. Khi ChatterBot nhận được nhiều đầu vào hơn, số lượng câu trả lời mà nó có thể trả lời và độ chính xác của mỗi câu trả lời liên quan đến câu lệnh đầu vào tăng lên. Chương trình chọn câu trả lời phù hợp nhất bằng cách tìm kiếm câu lệnh phù hợp nhất đã biết khớp với đầu vào, sau đó trả về câu trả lời có nhiều khả năng nhất cho câu lệnh đó dựa trên tần suất mỗi câu trả lời được đưa ra bởi những người mà bot giao tiếp.

## Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/ChatterBot) by running:

```
pip install chatterbot
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

ChatterBot comes with a data utility module that can be used to train chat bots.
At the moment there is training data for over a dozen languages in this module.
Contributions of additional training data or training data
in other languages would be greatly appreciated. Take a look at the data files
in the [chatterbot-corpus](https://github.com/gunthercox/chatterbot-corpus)
package if you are interested in contributing.

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

Xem tài liệu tại [đây](https://chatterbot.readthedocs.io/)

# Reference

See release notes for changes https://github.com/gunthercox/ChatterBot/releases
