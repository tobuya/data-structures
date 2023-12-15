"""The below modules will help create a basic visual representation of a stack."""
import matplotlib.pyplot as plt

class StackVisualization:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        fig, ax = plt.subplots()
        ax.set_title('Stack Visualization')
        ax.set_xlabel('Stack')
        ax.set_xticks([])
        ax.set_yticks([])

        stack_elements = list(reversed(self.stack))
        for i, element in enumerate(stack_elements):
            color = plt.cm.viridis(i / len(self.stack))  # Generating different colors
            ax.add_patch(plt.Rectangle((0, i), 1, 0.8, color=color, alpha=0.7))
            ax.text(
                0.5, i + 0.4, str(element), ha='center', va='center', color='black', fontsize=12
                )

        ax.plot([0, 0], [0, len(self.stack)], color='black')  # Vertical line representing the stack

        plt.show()

stack_vis = StackVisualization()
stack_vis.push(5)
stack_vis.push(10)
stack_vis.push(15)
stack_vis.push(20)
stack_vis.display()
