"""The below modules will help create a basic visual representation of a queue."""
import matplotlib.pyplot as plt

class QueueVisualization:
    def __init__(self):
        self.queue = []
   
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        fig, ax = plt.subplots()
        ax.set_title('Queue Visualization')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        
        if self.is_empty():
            ax.text(0.5, 0.5, 'Queue is Empty', ha='center', va='center', fontsize=12)
        else:
            values = self.queue[::-1]  # Reverse to display as a queue
            ax.bar(range(len(values)), values)
        
        plt.show()


queue_vis = QueueVisualization()
queue_vis.enqueue(5)
queue_vis.enqueue(10)
queue_vis.enqueue(15)
queue_vis.display()

queue_vis.dequeue()
queue_vis.display()
