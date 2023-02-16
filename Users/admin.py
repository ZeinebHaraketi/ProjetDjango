from django.contrib import admin,messages
from .models import Person

# Register your models here.
class JoinDateFilter (admin.SimpleListFilter):
 title='Join Date'
 parameter_name='date_joined'
def lookups(self, request, model_admin):
    return(
        ('Past', ('joined in the past')),
        ('Present', ('joined today') )
 )
def queryset (self, request, queryset):
   if self.value () =='Past':
     return queryset.filter(date_joined_lt=datetime.date.today())
   if self. value ()=='Present':
    return queryset.filter(date_joined_exacte=datetime.date.today())
   

class Admin(admin.ModelAdmin):
    def inactive(self,request,queryset):
        
        rows_filter=queryset.filter(is_active=False)
        
        if rows_filter.count()>0:
            messages.error(request,message=f"{rows_filter.count()} are already inactive")
            
        else:
           rows=queryset.update(is_active=False)
           if (rows ==1):
                 msg="One User Was"
           else:
                  msg=f"{rows} users were"
           messages.success(request,message='%s successfully active'% msg)
    #inactive.short_description="" #pour modifier  affichage de nom de def
    actions=["inactive"]      
    list_display=(
        'cin',
        'email',
        'username',
        'is_active'
    )
    list_filter =(
        'cin',
        'email',
        'username',
        JoinDateFilter,
       
    )
    #trie by ordre alphabitique selon le titre 
    ordering =('cin',)
    search_fields =[
        'cin',
        'email',
        'username',
    ]
    
    fieldsets = (
        (
            'Person',
            {
                'classes': ('collapse',),
                'fields': (
                    'email',
                    'cin',
                    'password',
                    'username',
                    'date_joined'
                    
                    
                ),
            }
        ),
        (
            'AbstractUser',
            {
                'classes': ('collapse',),
                'fields': (
                    'first_name',
                    'last_name',
                    'is_active',
                    'is_staff',
                    
                ),
            }
        ),
        
    )
admin.site.register(Person,Admin)

