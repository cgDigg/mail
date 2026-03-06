from .web import *
def push_mail(to_ip,message):
    push_tcp(to_ip,20263,message)