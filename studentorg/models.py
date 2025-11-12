class Program(BaseModel):
    prog_name = models.CharField(max_length=150, verbose_name="Program")
    college = models.ForeignKey(College, on_delete=models.CASCADE)

class Student(BaseModel):
    student_id = models.CharField(max_length=15, verbose_name="Student ID")
    lastname = models.CharField(max_length=25, verbose_name="Last Name")
    firstname = models.CharField(max_length=25, verbose_name="First Name")
    middlename = models.CharField(max_length=25, blank=True, null=True, verbose_name="Middle Name")
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
