from django.contrib import admin
from demo.book_a.models import Contact, Mail, SentMail
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email_id', 'first_name', 'last_name')
    search_fields = ('email_id', 'first_name', 'last_name')
    list_filter = ('last_name',)
    
class MailAdmin(admin.ModelAdmin):
    list_display = ('date_sent', 'sent_by', 'subject')
    search_fields = ('subject', 'body')
    list_filter = ('date_sent',)
    
class SentMailAdmin(admin.ModelAdmin):
    list_display = ('sent_to', 'mail', 'read', 'date_read')
    list_filter = ('date_read','read')
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(SentMail, SentMailAdmin)

