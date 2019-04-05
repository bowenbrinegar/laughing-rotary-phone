from django.db import models

class Flight(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=35)
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "username": self.username
        }

class FlightTracker(models.Model):
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'service'

    created = models.DateTimeField(auto_now_add=True)
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    avg_dist_to_potential_collision = models.IntegerField()
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
    objects = models.Manager()

    def as_dict_response(self):
        return {
            "id": self.id,
            "created": self.created,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos,
            "avg_dist_to_potential_collision": self.avg_dist_to_potential_collision,
            "flight_id": self.flight_id
        }