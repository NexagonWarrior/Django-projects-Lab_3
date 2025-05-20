from django.db import models

class stud_list(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    grade1 = models.IntegerField()
    grade2 = models.IntegerField()
    grade3 = models.IntegerField()
    grade4 = models.IntegerField()
    grade5 = models.IntegerField()
    scholarship = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Список студентів"

    def __str__(self):
        return f"{self.name} ({self.group})"
