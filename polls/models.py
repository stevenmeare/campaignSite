from django.db import models

# Create your models here.

# Define the question class
class Question(models.Model):
    '''
        This model defines a question. 
        The question has a one-to-many relationship with the choice model.

        :param question_text: The text of the question.
        :type question_text: str

        :param pub_date: The date the question was published.
        :type pub_date: datetime

        :return: The text of the question.
        :rtype: str
        
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# Define the choice class
class Choice(models.Model):
    '''
        This model defines a choice. 
        The choice has a many-to-one relationship with the question model.

        :param question: The question the choice is associated with.
        :type question: Question

        :param choice_text: The text of the choice.
        :type choice_text: str

        :param votes: The number of votes for the choice.
        :type votes: int

        :return: The text of the choice.
        :rtype: str
        
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text