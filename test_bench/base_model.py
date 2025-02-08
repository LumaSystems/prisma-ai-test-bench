import time
from abc import ABC, abstractmethod


class BaseModelTest(ABC):

    execution_times = []
    model_name = None

    def __init__(self, model_name: str):
        self.model_name = model_name
        type(self).model_name = model_name

    @abstractmethod
    def load_pipeline(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @classmethod
    def timecheck(cls, func):
        """Decorator to measure execution time of a method and store results."""

        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            cls.execution_times.append(
                {
                    "class": args[0].__class__.__name__,
                    "method": func.__name__,
                    "execution_time": execution_time,
                }
            )
            return result

        return wrapper

    @classmethod
    def report_execution_times(cls):
        if not cls.execution_times:
            print("No execution times recorded.")
            return

        print(f"\nExecution Time Report for Model: {cls.model_name or 'Unknown'}")
        for record in cls.execution_times:
            print(
                f"Class: {record['class']}, Method: {record['method']}, Time: {record['execution_time']:.4f} seconds"
            )
