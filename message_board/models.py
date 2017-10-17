from django.db import models

class MessageBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    message_board = models.ForeignKey(MessageBoard, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    handle_name = models.CharField(max_length=100)
