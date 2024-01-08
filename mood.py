from flask import Flask, redirect, url_for, render_template, session, Response
from flask import Blueprint, request, Request

app = Flask(__name__)

totvotes = 0 #total votes
votes = [] #votes that are not tired/stressed (numbers)
votesm = 0 #votes tired
votesg = 0 #votes stressed
pictures = {1:'Lachend.jpeg', 2:'gluecklich.jpeg', 3:'normal.jpeg', 4:'Traurig.jpeg', 5:'Weinend.jpeg'} #pictures corresponding to the average of votes

@app.route("/results/")
def endResult():
    global votes
    global totvotes
    global votesm
    global votesg
    percm = 0 #percentage tired
    percg = 0 #percentage stressed
    if len(votes) != 0:
        average = round(sum(votes) / len(votes)) #average of votes, rounded on entire numbers (1-5)
    else:
        average = 3 #if no votes/only votes for tired or stressed
    if votesm != 0:
        percm = round((100 / totvotes) * votesm) #percentage müde
    if votesg != 0:
        percg = round((100 /totvotes) * votesg) #percentage gestresst
    print('votesm =', votesm)           #testing purposes
    print('totvotes =', totvotes)       #
    print('average =', average)         #
    print('percm =', percm)             #
    print('votes:', votes)              #
    print(pictures[average])            #
    #return '{} {} {}'.format(str(pictures[average]), str(percm), str(percg))      #
    return render_template('result.html', picture = pictures[average], percentage_muede = percm, percentage_gestresst = percg)

@app.route('/api/vote/<result>/', methods=['POST'])
def api(result): #votes that aren't tired/stressed return a number between 1 and 5 in result
    global totvotes
    totvotes += 1 # +1 total vote
    votes.append(int(result)) #add this vote to list of votes
    return redirect('/results/') #redirect to result site

@app.route('/api/votes/m/', methods = ['POST'])
def apim(): #votes for tired
    global votesm
    global totvotes
    votesm += 1 # +1 vote for tired
    totvotes += 1
    return redirect('/results/')

@app.route('/api/votes/g/', methods = ['POST'])
def apig(): #votes for stressed
    global totvotes
    global votesg
    votesg += 1 # +1 vote for stressed
    totvotes += 1
    return redirect('/results/')

@app.route('/')
def home():
    return render_template('vote.html') #template


if __name__ == '__main__':
    app.run()