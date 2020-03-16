from django.db import models

class Campus(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.TextField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.campus.name}: {self.name}'

class Button(models.Model):
    SINGLE = 0
    DOUBLE = 1
    LONG = 2
    CLICK_CHOICES = (
        (SINGLE, 'Single'),
        (DOUBLE, 'Double'),
        (LONG, 'Long'),
    )
    # button_id = models.TextField()
    name = models.TextField(max_length = 100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time_clicked = models.DateTimeField(auto_now=True)
    click_type = models.PositiveSmallIntegerField(choices=CLICK_CHOICES)
    battery = models.PositiveSmallIntegerField()

    def _get_button_id(self):
        return f'{self.location.campus.name}: {self.location.name}: {self.name}'

        
    button_id = property(_get_button_id)

    # @property
    # def button_id(self):
    #     return f'{self.location.campus.name}: {self.location.name}: {self.name}'
    
    def __str__(self):
        return f'{self.location.campus.name}: {self.location.name}: {self.name}'

   