from django.db import models
from account.models import Account, Medium, Document


# from villa.models import Medium


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    account1 = models.ForeignKey(Account, null=True, blank=True, related_name='account1',on_delete=models.SET_NULL)
    account2 = models.ForeignKey(Account, null=True, blank=True, related_name='account2',on_delete=models.SET_NULL)

    def __str__(self):
        return f"Chat {self.id}: {self.account1.__str__()} + {self.account2.__str__()}"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=False, blank=False)
    file = models.OneToOneField(Document, on_delete=models.CASCADE, null=False, blank=False)
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(null=False, blank=False, max_length=1000)
    time = models.DateTimeField(db_index=True, auto_now=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        if self.text is not None:
            return self.owner.__str__() + ": " + self.text
        else:
            return self.owner.__str__() + ": " + '--null--'


class Replay(models.Model):
    chat_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(Message,related_name='parent_message', null=False, blank=False,on_delete=models.CASCADE)
    replay = models.ForeignKey(Message,related_name='replay_message', null=False, blank=False,on_delete=models.CASCADE)
