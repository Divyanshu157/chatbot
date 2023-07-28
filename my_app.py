from flask import Flask, render_template,request
from nltk.chat.util import Chat


que1 = r'how are you'
answer1= [
    'i am good',
    'all well',
    'awesome'
]

que2= r'what can you do'
answer2=[
    'i can reply to your quries',
    'i am here to answer your question',
    'i can chat with you'
]

que3= r'(.*) your name'
answer3=[
    ' i am chatty',
    'my namr is chatty'
]

que4= r'(.*)mausam(.*)ba(.*)rish'
answer4 =[ 'it looks it will rain today' , 'barrish ka mausam hai', 'baarish ho sakti hai']

qa_pair=[
    (que1,answer1),
    (que2,answer2),
    (que3,answer3),
    (que4,answer4),
    
]

chatbot = Chat(qa_pair)


app = Flask(__name__)

@app.route('/')
def home():
    global chatbot
    
    query = request.args.get('query')
    # print(query)
    if query!=None:
        response=chatbot.respond(query)
        if response == None:
            response= "Sorrry i am not sure\n"
            
        
    else:
        response=" "
  
    # response = "upflairs"
    return render_template('index.html',result = response)



@app.route('/chatbot')
def chat():
    return "<h2>CHAT BOT<h2/>"




app.run(debug=True, use_reloader=False)