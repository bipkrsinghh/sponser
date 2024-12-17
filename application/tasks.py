from celery import shared_task



@shared_task(ignore_result=False) #if i keep it True then the result will not going to stored in backend
def say_hello():
    return "Say hello"
