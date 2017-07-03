from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	posted_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	#Adding a helper function to get all the comment for particular post
	def get_all_comments(self):
		comments = Comment.objects.filter(post=self)
		return comments	

class Comment(models.Model):
	post = models.ForeignKey('Post')
	comment_body = models.TextField()

	def __unicode__(self):
		return self.comment_body