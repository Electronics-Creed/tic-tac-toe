class Tic:

    def __init__(self):
        self.game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.z = 0

    def computer_turn(self):
        global a, b
        bestscore = 10
        for i in range(0, 3):
            for j in range(0, 3):
                occupied = self.check(i, j)
                if not occupied:
                    self.game[i][j] = 'O'
                    score = self.minimax(True)
                    self.game[i][j] = ' '
                    if score < bestscore:
                        a = i
                        b = j
                    bestscore = min(score, bestscore)

        self.game[a][b] = 'O'
        return a, b

    def check(self, i, j):
        if self.game[i][j] == 'X' or self.game[i][j] == 'O':
            return True
        elif self.game[i][j] == ' ':
            return False

    def minimax(self, maximizingPlayer):
        board = self.board_is_full()
        w = self.declareWinner()

        if board:
            return w
        if not board and (w == 1 or w == -1):
            return w
        if maximizingPlayer:
            maxeval = -10
            for i in range(0, 3):
                for j in range(0, 3):

                    occupied = self.check(i, j)

                    if not occupied:
                        self.game[i][j] = 'X'
                        eval = self.minimax(False)
                        self.game[i][j] = ' '
                        maxeval = max(eval, maxeval)

            return maxeval
        else:
            mineval = 10
            for m in range(0, 3):
                for n in range(0, 3):

                    occupied = self.check(m, n)

                    if not occupied:
                        self.game[m][n] = 'O'
                        eval = self.minimax(True)
                        self.game[m][n] = ' '
                        mineval = min(eval, mineval)

            return mineval

    def declareWinner(self):
        u = 0
        while u < 3:

            if self.game[u][0] == self.game[u][1] == self.game[u][2] == 'X':
                return 1
            elif self.game[u][0] == self.game[u][1] == self.game[u][2] == 'O':
                return -1
            if self.game[0][u] == self.game[1][u] == self.game[2][u] == 'X':
                return 1
            elif self.game[0][u] == self.game[1][u] == self.game[2][u] == 'O':
                return -1
            u += 1

        if self.game[0][0] == self.game[1][1] == self.game[2][2] == 'X':
            return 1
        elif self.game[0][0] == self.game[1][1] == self.game[2][2] == 'O':
            return -1
        if self.game[0][2] == self.game[1][1] == self.game[2][0] == 'X':
            return 1
        elif self.game[0][2] == self.game[1][1] == self.game[2][0] == 'O':
            return -1

        return 0

    def board_is_full(self):
        for i in range(0, 3):
            for j in range(0, 3):
                occupied = self.check(i, j)

                if not occupied:
                    return False
        return True


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(2), nullable=False)
    y = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return self.x + self.y


tic = Tic()
row = [
    {"col1": " ", "col2": " ", "col3": " "}, {"col1": " ", "col2": " ", "col3": " "},
    {"col1": " ", "col2": " ", "col3": " "}
]


@app.route('/', methods=["GET", 'POST'])
def index():
    if request.method == 'POST':
        while True:
            post_x = request.form["x"]
            post_y = request.form["y"]
            new_post = BlogPost(y=post_y, x=post_x)

            if not (tic.game[int(post_x)][int(post_y)] == 'X' or tic.game[int(post_x)][int(post_y)] == 'O'):  # check if space is occupied in html
                tic.game[int(post_x)][int(post_y)] = "X"

                if post_x == '0':
                    row[int(post_y)]["col1"] = "X"
                elif post_x == '1':
                    row[int(post_y)]["col2"] = "X"
                elif post_x == '2':
                    row[int(post_y)]["col3"] = "X"

                a, b = tic.computer_turn()  # computer turn
                if a == 0:
                    row[b]["col1"] = "0"
                elif a == 1:
                    row[b]["col2"] = "0"
                elif a == 2:
                    row[b]["col3"] = "0"

                db.session.add(new_post)
                db.session.commit()

                break
            else:
                return render_template('index.html', row=row, para="place taken")

        declare = tic.declareWinner()  # check for win
        if declare == 1:
            print('You have won the game')
            return render_template('index.html', row=row, para="You have won the game")
        elif declare == -1:
            print('Computer has won the game')
            return render_template('index.html', row=row, para="You have lost the game")
        if tic.board_is_full():
            if tic.declareWinner() == 0:
                return render_template('index.html', row=row, para="playing")

        return render_template('index.html', row=row, para="your turn")
    else:
        return render_template('index.html', row=row)


if __name__ == "__main__":
    app.run(debug=True)

