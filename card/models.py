from django.db import models

# Create your models here.
NUM_BOX = 5
BOXES = range(1, NUM_BOX  + 1) 

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES,BOXES),
    )
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question
    

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if self.box in BOXES:
            self.box = new_box
            self.save()
            
        return self
