from celery import Celery 
app = Celery()

@app.task
def add(x, y):
    return x + y

if __name__=='__main__':
    app.start()