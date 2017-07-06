from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver



class Problem(models.Model):
    author = models.ForeignKey(User)
    anonymous_author = models.BooleanField(default=False)
    problem = models.ForeignKey('self',related_name='problems', null=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    downvotes = models.ManyToManyField(User, related_name='downvotes')
    in_response_to = models.TextField()

    def count_subproblems(self):
        def count_subs(problem):
            count = 0
            if problem.problems:
                for p in problem.problems.all():
                    count = count + 1
                    count = count + count_subs(p)
            return count

        return count_subs(self)


    def overall_votes(self):
        def recursive_upvotes(problem):
            upvotelist = self.upvotes.all()
            if problem.problems:
                for p in problem.problems.all():
                    upvotelist = list(set(list(upvotelist) + list(p.upvotes.all())))
                    upvotelist = list(set(list(upvotelist) + list(recursive_upvotes(p))))
            return upvotelist
        def recursive_downvotes(problem):
            downvotelist = self.downvotes.all()
            if problem.problems:
                for p in problem.problems.all():
                    downvotelist = list(set(list(downvotelist) + list(p.downvotes.all())))
                    downvotelist = list(set(list(downvotelist) + list(recursive_downvotes(p))))
            return downvotelist
        return len(recursive_upvotes(self)) - len(recursive_downvotes(self))


    def present_overall_votes(self):
        presenting_problem = self
        if self.has_parent() == True:
            has_parent = True
            problemloop = self
            while (has_parent == True):
                presenting_problem = problemloop.problem
                if problemloop.problem.has_parent():
                    has_parent = True
                    problemloop = problemloop.problem
                else:
                    has_parent = False
        return presenting_problem.overall_votes()



    def total_why_requests(self):
        return self.why_requests.count()

    def has_parent(self):
        if self.problem:
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

class WhyRequest(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='why_requests', null=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='why_request_likes')

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='comments', null=True)
    # is_problem_comment = models.BooleanField(default = True)
    # why = models.ForeignKey('problems.Why', related_name='comments', null=True)
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
