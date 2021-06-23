from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=10)
    longname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Telescope(models.Model):
    name = models.CharField(max_length=10)
    longname = models.CharField(max_length=100)

    def __str__(self):
        return self.name
  
class Backend(models.Model):
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    longname = models.CharField(max_length=100)

    def __str__(self):
        return "{}/{}".format(self.telescope.name, self.name)

class Astronomer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Proposal(models.Model):
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    principal_investigator = models.ForeignKey(Astronomer, on_delete=models.CASCADE)
    year = models.IntegerField()
    cycle = models.IntegerField()
    date_submitted = models.DateField()
    date_decided = models.DateField()
    accepted = models.BooleanField()
    filename = models.CharField(max_length=250)

    def __str__(self):
        return "{}/{}".format(self.telescope.name, self.code)

class Session(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    observer = models.ForeignKey(Astronomer, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    backend = models.ForeignKey(Backend, on_delete=models.CASCADE)
    setupfile = models.CharField(max_length=250)
    commandfile = models.CharField(max_length=250)

    def __str__(self):
        return "{}_starting_from_{}".format(self.proposal, self.start_time)

class SourceType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=10)
    srctype = models.ForeignKey(SourceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DataFormat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Observation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    lofreq = models.FloatField()
    bandwidth = models.FloatField()
    nbit = models.IntegerField()
    nchan = models.IntegerField()
    tsmpl = models.FloatField()
    usb = models.BooleanField()
    npol = models.IntegerField()
    interferometer_mode = models.CharField(max_length=2)
    coherent_dedispersion = models.BooleanField()
    data_format = models.ForeignKey(DataFormat, on_delete=models.CASCADE)
    data_filename = models.CharField(max_length=250)
    interferometry_filename = models.CharField(max_length=250, null=True, blank=True)
    timestamp_filename = models.CharField(max_length=250)
    start_time = models.DateTimeField()
    duration = models.FloatField()

    def __str__(self):
        return "{}_observation_of_{}_starting_from_{}".format(self.proposal, self.pulsar, self.start_time)

class Archive(models.Model):
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
    data_format = models.ForeignKey(DataFormat, on_delete=models.CASCADE)
    filename = models.CharField(max_length=250)
    analyzer = models.ForeignKey(Astronomer, on_delete=models.CASCADE)

