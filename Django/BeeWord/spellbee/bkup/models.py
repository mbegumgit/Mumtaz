from django.db import models

# Create your models here.

class BeeWord(models.Model):
	level = models.CharField(max_length=5)
	word = models.CharField(max_length=90)

	def __str__(self):
		return f"Difficulty level {self.level} - ({self.word})"

class CustomBooleanField(models.BooleanField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1
        
class Score(models.Model):
	word = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="scoreboard")
    lastscore = models.IntegerField()