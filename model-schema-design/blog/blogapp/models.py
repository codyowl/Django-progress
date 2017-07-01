from django.db import models

#Just a simple blog app which will contains two models.
#1.BlogPost(for getting blog details)
#2.Category(for getting category details of the blog entries)

class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	posted = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category')

	def __unicode__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=200)	

	def __unicode__(self):
		return self.title
		