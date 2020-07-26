import threading
import time

lock = threading.Lock()
class Movieticket:
    def __init__(self,name,seatnum,row):
        self.name = name
        self.seatnum = seatnum
        self.row = row

    def movieticket(self):
        print('{}\t{}\t{}\t'.format(self.name,self.seatnum,self.row))

class Bookingticket(threading.Thread):
    def selfmovieticket(self,ticket,email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
