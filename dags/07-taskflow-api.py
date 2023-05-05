from airflow.decorators import dag, task
import timeit

def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Antes de executar a minha funcao principal")
        result = func(*args, **kwargs)
        print("Depois de executar a minha funcao principal")

        return result
    
    return wrapper


def timeit_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    
    return wrapper


@timeit_decorator
def soma(x,y):
    return x + y

soma(1,2)