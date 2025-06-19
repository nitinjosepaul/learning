import random
from queue import Queue


class PrintQueue(Queue):
    pass


class Job:
    def __init__(self):
        self.pages = random.randint(1, 10)

    def print_page(self):
        print("Printed %s" % str(self.pages))
        self.pages -= 1

    def check_complete(self):
        return self.pages == 0


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue_obj):
        if not print_queue_obj.is_empty():
            self.current_job = print_queue_obj.dequeue()
            return True
        else:
            print("No more jobs left!")
            self.current_job = None
            return False

    def print_job(self, job):
        if job:
            while not job.check_complete():
                job.print_page()
        else:
            print("Invalid print job!")



printqueue1 = PrintQueue()
job1 = Job()
job2 = Job()
printqueue1.enqueue(job1)
printqueue1.enqueue(job2)

printer1 = Printer()
print("FIRST PRINT")
printer1.get_job(printqueue1)
printer1.print_job(printer1.current_job)

print("SECOND PRINT")
printer1.get_job(printqueue1)
printer1.print_job(printer1.current_job)

print("THIRD PRINT")
printer1.get_job(printqueue1)
printer1.print_job(printer1.current_job)
