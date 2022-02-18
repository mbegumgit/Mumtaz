from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class BeeWord(db.Model):
    #title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    __tablename__ = "Words"
    id = db.Column('Bee_id', db.Integer, primary_key = True)
    level = db.Column(db.String(10),nullable=False)
    word = db.Column(db.String,db.ForeignKey("Scores.id"),nullable=False) 
    pick_idx =db.Column(db.Integer)
class BeeScore(db.Model):
    __tablename__= "Scores"
    word = db.Column(db.String(100),  primary_key = True)
    score_board_1 = db.Column(db.Integer(1))
    score_board_2 = db.Column(db.Integer(1))
    score_board_3 = db.Column(db.Integer(1))
    score_board_4 = db.Column(db.Integer(1))
    score_board_5 = db.Column(db.Integer(1))
    last_score = db.Column(db.Integer(1))

    # def __init__(self, id, level, word, pick_idx):
        # self.id = id
        # self.level = level
        # self.word = word
        # self.pick_idx= pick_idx

    # def __repr__(self):
        # return "Spell Bee: {}\tLDifficultyLevel :{}\t".format(self.word,self.level)