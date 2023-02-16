from django.contrib import admin,messages
from .models import Event, Participation

# Register your models here.
class DateFilter (admin.SimpleListFilter):
 title='Events Date'
 parameter_name='dateEvent'
def lookups(self, request, model_admin):
    return(
        ('Past', ('past event')),
        ('Present', ('present event') ),
        ('Futur', ('Futur event') )
 )
def queryset (self, request, queryset):
   if self.value () =='Past':
     return queryset.filter(dateEvent_lt=datetime.date.today())
   if self. value ()=='Present':
    return queryset.filter(dateEvent_exacte=datetime.date.today())
   if self.value ()=='Futur':
      return queryset.filter(dateEvent_gt=datetime.date.today())
class ParticipantFilter(admin.SimpleListFilter):
    title='Participants'
    parameter_name='nbParticipants'

    def lookups(self, request, model_admin): 
        return (
            ('0',('No Participants')),
            ('more',('There are Participants')),
        )
    def queryset(self, request, queryset):
        if self.value()=='0':
           return queryset.filter(nbParticipants__exacte=0)       
        if self.value()=='more':
            return queryset.filter(nbParticipants__gt=0) 
class ParticipationInLine(admin.StackedInline):
    model=Participation
    extra=1 #par defaut 3lignes avex extra 1ligne
    classes=['collapse'] #collapse les classes caches
    can_delete=True
    readonly_fields=('datePart',)
def set_state(ModelAdmin,request,queryset):
    rows=queryset.update(state=True)
    if(rows ==1):
        msg="One Event Was"
    else:
        msg=f"{rows} events were"
    messages.success(request,message='%s successfully accepted'% msg) 
set_state.short_description="Accept" #pour modifier affichage de def

class EventAdmin(admin.ModelAdmin):
    def unset_state(self,request,queryset):
        
        rows_filter=queryset.filter(state=False)
        
        if rows_filter.count()>0:
            messages.error(request,message=f"{rows_filter.count()} are already refused")
            
        else:
           rows=queryset.update(state=False)
           if (rows ==1):
                 msg="One Event Was"
           else:
                  msg=f"{rows} events were"
           messages.success(request,message='%s successfully accepted'% msg) 
              #messages.error(request,message='%s successfully refused'% msg) 

    unset_state.short_description="Refuse" #pour modifier  affichage de nom de def
    actions=[set_state ,"unset_state"]
    actions_on_bottom=True #action et on top et on bottom pour gerer les grandes listes
    inlines=[
        ParticipationInLine
    ]
    list_per_page=20
    list_display=(
        'title',
        'category',
        'state',
    )
    list_filter =(
        'state',
        'category',
        ParticipantFilter,
        DateFilter
    )
    #trie by ordre alphabitique selon le titre 
    ordering =('title',)
    search_fields =[
        'titre',
        'category'
    ]
    readonly_fields =('createdAt',)
    autocomplete_fields=['organized']
    fieldsets = (
        (
            'State',
            {
                'fields': ('state',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'title',
                    'imageEvent',
                    'category',
                    'organized',
                    'nbParticipants',
                    'description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'dateEvent',
                        'createdAt'
                    ),
                )
            }
        ),
    )
admin.site.register(Event,EventAdmin)
