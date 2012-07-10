from django.contrib import admin

from django.db import models

from datetime import date

# Create your models here.


class Post(models.Model):

    title=models.CharField(max_length = 70)

    body=models.TextField()

    created=models.DateField()
    updated=models.DateField()
#    def __unicode__(self):
#		return self.title

class Blog(models.Model):

    body=models.TextField()

    author=models.CharField(max_length=70)
     
   # date = models.DateField(_("Date"), auto_now_add=True)



    created=models.DateField()
    updated=models.DateField()

    post=models.ForeignKey(Post,related_name = 'Post')
#    def body_first_70(self):
#		return self.body[:70]
#	def __unicode__(self):
#		return self.author

class BlogInline(admin.TabularInline):
	model=Blog
	

class PostAdmin(admin.ModelAdmin):
   
   list_display =('title','created','updated')
   search_fields = ('title','body')
   list_filter = ('created','title')
   inlines = [BlogInline]

	

class BlogAdmin(admin.ModelAdmin):
	list_display=('post','author','body','created','updated')
	list_filter=('created','author')
   
   

    
admin.site.register(Post,PostAdmin)
admin.site.register(Blog,BlogAdmin)


    
