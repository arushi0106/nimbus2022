from django.db import models

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,is_active=True,is_student = False, is_teacher = False,is_principal = False ,is_staff=False, is_admin= False):
        if not email:
            raise ValueError("User must have a valid email address")
        if not password:
	@@ -19,7 +19,7 @@ def create_user(self,email,password=None,is_active=True,is_student = False, is_t
        user_obj.is_active = is_active
        user_obj.is_student = is_student
        user_obj.is_teacher = is_teacher
        user_obj.is_principal = is_principal
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.save(using=self._db)
	@@ -57,7 +57,7 @@ class User(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'