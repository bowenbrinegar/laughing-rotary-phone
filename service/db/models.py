from django.db import models

class Flight(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=35)
    score = models.IntegerField(default=0)
    livesLeft = models.IntegerField(default=0)
    timeLeft = models.IntegerField(default=0)
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "username": self.username,
            "score": self.score,
            "livesLeft": self.livesLeft,
            "timeLeft": self.timeLeft,
        }

class SpeedData(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    speed = models.IntegerField()
    time = models.IntegerField()
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="speed")
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "speed": self.speed,
            "time": self.time,
        }

class PositionData(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    x_pos = models.FloatField(default=0)
    y_pos = models.FloatField(default=0)
    time = models.IntegerField(default=0)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="position")

    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos,
            "time": self.time,
        }

class HoopsBundle(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField(default=0)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="hoops")
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "time": self.time,
        }

class HoopData(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    hoop_id = models.ForeignKey(HoopsBundle, on_delete=models.CASCADE, related_name="hoops_data")
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos,
        }


class AsteriodsBundle(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField(default=0)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="asteriods")
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "time": self.time,
        }

class AsteriodData(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    asteriod_id = models.ForeignKey(AsteriodsBundle, on_delete=models.CASCADE, related_name="asteriods_data")
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos,
        }