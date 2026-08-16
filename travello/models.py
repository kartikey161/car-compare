from django.db import models

class Destination(models.Model):
    comp = models.CharField(max_length=100, default="None")
    name = models.CharField(max_length=100, default="None")
    img = models.ImageField(upload_to='pics')
    decs = models.TextField(default="None")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Images(models.Model):
    name = models.CharField(max_length=100, default="None")
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Sales(models.Model):
    name = models.CharField(max_length=100, default="None")
    sale = models.IntegerField()
    date = models.CharField(max_length=100, default="None")
    def __str__(self):
        return self.name

class KeyFeat(models.Model):
    name = models.CharField(max_length=100)
    Power_Steering = models.BooleanField(default=False)
    Rear_Suspension = models.BooleanField(default=False)
    Front_Suspension = models.BooleanField(default=False)
    Auto_Climate_Control = models.BooleanField(default=False)
    Alloy_Wheels = models.BooleanField(default=False)
    Power_Windows = models.BooleanField(default=False)
    Air_Conditioner = models.BooleanField(default=False)
    Passenger_Airbag = models.BooleanField(default=False)
    Fog_Lights = models.BooleanField(default=False)
    Heater = models.BooleanField(default=False)
    Adjustable_Steering = models.BooleanField(default=False)
    Air_Quality = models.BooleanField(default=False)
    Remote = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class KeySpecs(models.Model):
    name = models.CharField(max_length=100)
    Mileage = models.CharField(max_length=100)
    Max_Power = models.CharField(max_length=100)
    Seats = models.CharField(max_length=100)
    Service_Cost = models.CharField(max_length=100)
    Tank_Capacity = models.CharField(max_length=100)
    Transmission_Type = models.CharField(max_length=100)
    Fuel_Type = models.CharField(max_length=100)
    Engine_Displacement = models.CharField(max_length=100)
    Body_Type = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class EngineTrans(models.Model):
    name = models.CharField(max_length=100)
    No_cylinder = models.CharField(max_length=100)
    Turbo_Charger = models.BooleanField(default=False)
    Super_Charge = models.BooleanField(default=False)
    Gear_Box = models.CharField(max_length=100)
    Drive_Type = models.CharField(max_length=100)
    Tank_Capacity = models.CharField(max_length=100)
    Valve_Configuration = models.CharField(max_length=100)
    Fuel_Supply = models.CharField(max_length=100)
    Valves_Cylinder = models.CharField(max_length=100)
    Max_Torque = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FuelPerf(models.Model):
    name = models.CharField(max_length=100)
    Top_Speed = models.CharField(max_length=100)
    Turbo_Charger = models.BooleanField(default=False)
    Super_Charge = models.BooleanField(default=False)
    Turning_Radius = models.CharField(max_length=100)
    Acceleration = models.CharField(max_length=100)
    Front_Brake = models.CharField(max_length=100)
    Rear_Brake = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class DimensionsCap(models.Model):
    name = models.CharField(max_length=100)
    Length = models.CharField(max_length=100)
    Width = models.CharField(max_length=100)
    Height = models.CharField(max_length=100)
    Boot_Space = models.CharField(max_length=100)
    Ground_Clearance = models.CharField(max_length=100)
    Wheel_Base = models.CharField(max_length=100)
    Front_Tread = models.CharField(max_length=100)
    Rear_Tread = models.CharField(max_length=100)
    Gross_Weight = models.CharField(max_length=100)
    No_Doors = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Entertainment_Comm(models.Model):
    name = models.CharField(max_length=100)
    Cd_Player = models.BooleanField(default=False)
    CD_Changer = models.BooleanField(default=False)
    DVD_Player = models.BooleanField(default=False)
    Radio = models.BooleanField(default=False)
    No_Speakers = models.CharField(max_length=100)
    Integrated_2DIN = models.BooleanField(default=False)
    USB_Auxiliary_input = models.BooleanField(default=False)
    Bluetooth_Connectivity = models.BooleanField(default=False)
    Touch_Screen = models.BooleanField(default=False)
    Internal_Storage = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Home(models.Model):
    Comp = models.CharField(max_length=100)
    Dis = models.TextField()
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.Comp

class Feedback(models.Model):
    c_name = models.CharField(max_length=100)
    comp = models.CharField(max_length=100, default="None")
    name = models.CharField(max_length=100, default="None")
    price = models.IntegerField()
    int_design = models.IntegerField()
    ext_design = models.IntegerField()
    mileage = models.IntegerField()
    service_cost = models.IntegerField()
    safety_score = models.IntegerField()
    suggestion = models.TextField(max_length=250)
    def __str__(self):
        return self.name

class Comp_result(models.Model):
    value = models.CharField(max_length=100)
class Meta:
    db_table = "Destination", "Images", "Sales", "Key_Feat", "Key_Specs", "Engine_Trans", "Fuel_Perf", "Dimensions_Cap", "Entertainment_Comm", "Home", "Feedback"