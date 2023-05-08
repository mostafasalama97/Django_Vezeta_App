from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext as _


TYPE_OF_PERSON =(
    ( 'M' , "Male"),
    ( 'F' , "Female"),
    )

class Profile(models.Model):

    DOCTOR_IN={
        ( "جلدية" , "جلدية"),
        ( "أسنان" , "أسنان"),
        ( "نفسي" , "نفسي"),
        ( "أطفال حديثي الولادة"  , "أطفال حديثي الولادة"),
        ( "مخ وأعصاب"  , "مخ وأعصاب"),
        (  "عظام" , "عظام"),
        ( "نساء وتوليد"  , "نساء وتوليد"),
        ( "أنف وأذن وحنجرة"   , "أنف وأذن وحنجرة"),
        ( "قلب وأوعيه دموية"   , "قلب وأوعيه دموية"),
        ( "أمراض دم" , "أمراض دم"),
        ( "أورام" , "أورام"),
        ( "باطنة" , "باطنة"),
        ( "تخسيس وتغذية"  , "تخسيس وتغذية"),
        ( "جراحة أطفال"  , "جراحة أطفال"),
        ( "جراحة أورام"  , "جراحة أورام"),
        ( "جراحة أوعيه دموية"   , "جراحة أوعيه دموية"),
        ( "جراحة تجميل"  , "جراحة تجميل"),
        ( "جراحة سمنة ومناظير "   , "جراحة سمنة ومناظير "),
    }
    user            = models.OneToOneField(User,  on_delete=models.CASCADE)
    who_i           = models.TextField(_("من انا"), max_length=250)
    name            = models.CharField(_("الإسم رابعى"), max_length=50)
    surname         = models.CharField(_("اللقب"), max_length=20, blank=True, null=True) 
    subtitle        = models.TextField(_("نبذه عنك"), max_length=70, blank=True, null=True)
    address         = models.CharField(_("المحافظه"), max_length=30, blank=True, null=True)
    address_detail  = models.CharField(_("العنوان بالتفصيل"), max_length=25, blank=True, null=True)
    price           = models.IntegerField(_("سعر الكشف"), blank=True, null=True)
    number_phone    = models.CharField(_("رقم الهاتف"), max_length=50, blank=True, null=True)
    working_hours   = models.CharField(_("عدد ساعات العمل"), max_length=50, blank=True, null=True)
    img           = models.ImageField(_("profile_image"), blank=True, null=True)
    Waiting_time    = models.IntegerField(_("مده الانتظار"), blank=True, null=True)
    facebook        = models.CharField(max_length=100 , blank=True, null=True)
    twitter         = models.CharField(max_length=100 , blank=True, null=True)
    google          = models.CharField(max_length=100 , blank=True, null=True)
    join_us         = models.DateTimeField(_("وقت الانضمام") ,auto_now_add=True ,blank=True, null=True)
    type_doctors    = models.CharField(_("النوع"), choices=TYPE_OF_PERSON, default='M' ,max_length=20, blank=True, null=True)
    doctor          = models.CharField(_("دكتور ؟"),choices=DOCTOR_IN , max_length=50, blank=True, null=True)
    Specialist_doctor = models.CharField(_("متخصص فى ؟"), max_length=50, blank=True, null=True)
    rating          = models.PositiveIntegerField(_("التقييم"),default=0, blank=True, null=True)
    slug            = models.SlugField(_("slug") , blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return '%s' %(self.user.username)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)





class Comment(models.Model):
    comment     = models.ForeignKey('Profile' , related_name="author", on_delete=models.CASCADE, null=True, blank=True)
    create_at   = models.DateTimeField(auto_now_add=True , blank=True, null=True)
    name        = models.CharField(_("الإسم"), max_length=50)
    email       = models.EmailField(_("الإيميل"), max_length=50)
    comments    = models.TextField(_("التعليق") , max_length=250)

    def __str__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-create_at',)

class Appointment(models.Model):
    doctor      = models.ForeignKey('Profile',related_name="doc" , verbose_name=_("doctor"), on_delete=models.CASCADE  , blank=True, null=True)
    name        = models.CharField(_("الإسم") , max_length=100)
    number      = models.CharField(_("رقم الهاتف") , max_length=20)
    email       = models.EmailField(_("الإيميل"), max_length=50)
    read        = models.BooleanField(_("تمت القراءة"), blank=True, null=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    photo = models.ForeignKey("Profile", verbose_name=_("photo"), on_delete=models.CASCADE)
    clinic_photos = models.ImageField(_("صور العياده :"), blank=True, null=True)
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categorys")


