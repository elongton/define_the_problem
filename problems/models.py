from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver


class Problem(models.Model):
    author = models.ForeignKey(User)
    anonymous_author = models.BooleanField(default=False)
    rootproblem = models.ForeignKey('problems.Problem', related_name='subproblems', null=True, blank=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    downvotes = models.ManyToManyField(User, related_name='downvotes')

    def total_votes(self):
        return self.upvotes.count() - self.downvotes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('problems:problem_detail', kwargs={'pk':self.pk} )

    def __str__(self):
        return str(self.create_date)

class Comment(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes')

    def total_likes(self):
        return self.likes.count()

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('problems:problem_detail', kwargs={'pk':self.problem.pk} )

    def __str__(self):
        return self.text

class Reply(models.Model):
    comment = models.ForeignKey('problems.Comment', related_name='replies')
    author = models.ForeignKey(User)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_reply = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='reply_likes')

    def total_likes(self):
        return self.likes.count()

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('problems:problem_detail', kwargs={'pk':self.comment.problem.pk} )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "replies"
