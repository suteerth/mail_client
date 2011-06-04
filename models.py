from django.db import models

class Contact(models.Model):
    email_id = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField()
    contacts = models.ManyToManyField("self", blank=True)
    
    def __unicode__(self):
        return self.email_id
    
    class Meta:
        ordering = ['email_id']
        
class Mail(models.Model):
    subject = models.TextField()
    body = models.TextField()
    date_sent = models.DateTimeField()
    sent_by = models.ForeignKey(Contact, related_name="sent_by")
    sent_tos = models.ManyToManyField(Contact, related_name="sent_tos", through="SentMail")
    
    def __unicode__(self):
        return u'%s - %s' % (self.date_sent, self.subject)
    
    class Meta:
        ordering = ['sent_by', 'date_sent']
    
class SentMail(models.Model):
    sent_to = models.ForeignKey(Contact)
    mail = models.ForeignKey(Mail)
    read = models.BooleanField()
    date_read = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s - %s' %(self.sent_to, self.read)
    
    class Meta:
        ordering = ['sent_to', 'read', 'date_read']
        