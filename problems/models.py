from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver


class Problem(models.Model):
    author = models.ForeignKey(User)
    anonymous_author = models.BooleanField(default=False)
    root_problem = models.ForeignKey('self', related_name='sub_problems', null=True)
    # subproblem = models.ForeignKey('self', related_name='rootproblem')
    why_requests = models.ManyToManyField(User, related_name='problem_why_requests')
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    downvotes = models.ManyToManyField(User, related_name='downvotes')

    def total_why_requests(self):
        return self.why_requests.count()

    def has_root(self):
        if self.root_problem:
            return True
        else:
            return False

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
        return str(self.text)

class Comment(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='comments', null=True)
    why = models.ForeignKey('problems.Why', related_name='comments', null=True)
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

class Why(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='whys', null=True)
    author = models.ForeignKey(User, related_name='why_author', null=True)
    has_descendent = models.BooleanField(default=False)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    upvotes = models.ManyToManyField(User, related_name='why_upvotes')
    downvotes = models.ManyToManyField(User, related_name='why_downvotes')
    why_requests=models.ManyToManyField(User)
    depth = models.IntegerField(default=0)


    def total_votes(self):
        return self.upvotes.count() - self.downvotes.count()
