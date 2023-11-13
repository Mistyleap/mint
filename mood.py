from flask import Flask, redirect, url_for, render_template, session, Response
from flask import Blueprint, request, Request

app = Flask(__name__)

totvotes = 0
votes = []
votesm = 0

@app.route("/results/")
def endResult():
    global votes
    global totvotes
    global votesm
    percm = 0
    average = sum(votes[:]) / len(votes[:])
    if votesm != 0:
        percm = 100 / totvotes * votesm
    #print(votesm)
    #print(totvotes)
    #print(average)
    #print(percm)
    print(votes)
    return render_template('result.html', average = average, percm = percm)

@app.route('/api/vote/<result>/', methods=['GET'])
def api(result):
    global totvotes
    totvotes += 1
    print(result)
    votes.append(int(result))
    return redirect('/results/')

@app.route('/api/votes/m/')
def apim():
    global votesm
    global totvotes
    votesm += 1
    totvotes += 1
    return redirect('/results/')

@app.route('/')
def home():
    return render_template('vote.html')


if __name__ == '__main__':
    app.run()