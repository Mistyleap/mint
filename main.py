from flask import Flask, redirect, url_for, render_template, session, Response

app = Flask(__name__)

totvotes = 0 #total votes
votes = [] #votes that are not tired/stressed (numbers)
votesm = 0 #votes tired
votesg = 0 #votes stressed
pictures = {
                1:'Lachend.png', 
                2:'gluecklich.png', 
                3:'normal.png', 
                4:'Traurig.png', 
                5:'Weinend.png',
            } #pictures corresponding to the average of votes

@app.route("/results/")
def results():
    global votes
    global totvotes
    global votesm
    global votesg
    average = round(sum(votes) / len(votes)) if len(votes) else 3 #average of votes, rounded on entire numbers (1-5) else 3

    percm = round((100 / totvotes) * votesm) if totvotes else 0 #percentage müde
    percg = round((100 / totvotes) * votesg) if totvotes else 0 #percentage gestresst

    print(f'{votesm=}, {totvotes=}, {average=}, {percm=}, {votes}, imageName={pictures[average]}')           #testing purposes
    #return '{} {} {}'.format(str(pictures[average]), str(percm), str(percg))      #
    return render_template('result.html', picture = url_for('static', filename=f'images/{pictures[average]}'), percentage_muede = percm, percentage_gestresst = percg)

@app.route('/api/vote/<result>/', methods=['POST'])
def api(result): #votes that aren't tired/stressed return a number between 1 and 5 in result
    global totvotes
    totvotes += 1 # +1 total vote
    votes.append(int(result)) #add this vote to list of votes
    return redirect(url_for('results')) #redirect to result site

@app.route('/api/votes/m/', methods = ['POST'])
def apim(): #votes for tired
    global votesm
    global totvotes
    votesm += 1 # +1 vote for tired
    totvotes += 1
    return redirect(url_for('results'))

@app.route('/api/votes/g/', methods = ['POST'])
def apig(): #votes for stressed
    global totvotes
    global votesg
    votesg += 1 # +1 vote for stressed
    totvotes += 1
    return redirect(url_for('results'))

@app.route('/')
def home():
    return render_template('vote.html') #template


if __name__ == '__main__':
    app.run()