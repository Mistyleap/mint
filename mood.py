from flask import Flask, redirect, url_for, render_template, session, Response
from flask import Blueprint, request, Request

app = Flask(__name__)

totvotes = 0
votes = []
votesm = 0
votesg = 0
pictures = {1:'lachend.jpeg', 2:'gluecklich.jpeg', 3:'normal.jpeg', 4:'traurig.jpeg', 5:'weinend.jpeg'}
#funktioniert das? --> Loris fragen

@app.route("/results/")
def endResult():
    global votes
    global totvotes
    global votesm
    global votesg
    global pictures
    percm = 0
    average = sum(votes) / len(votes)
    rAverage = round(average)
    if votesm != 0:
        percm = round(100 / totvotes * votesm) #100 % funktioniert nicht
    if votesg != 0:
        percg = 100 /totvotes * votesg
    print(votesm)
    print(totvotes)
    print(average)
    print(percm)
    print(votes)
    print(pictures[rAverage])
    return(str(percm))
    #return render_template('result.html', average = pictures[rAverage], percm = percm, percg = percg)

@app.route('/api/vote/<result>/', methods=['POST'])
def api(result):
    global totvotes
    totvotes += 1
    print(result)
    votes.append(int(result))
    return redirect('/results/')

@app.route('/api/votes/m/', methods = ['POST'])
def apim():
    global votesm
    global totvotes
    votesm += 1
    totvotes += 1
    return redirect('/results/')

@app.route('/api/votes/g/', methods = ['POST'])
def apig():
    global totvotes
    global votesg
    votesg += 1
    totvotes += 1
    return redirect('/results/')

@app.route('/')
def home():
    return render_template('vote.html')


if __name__ == '__main__':
    app.run()