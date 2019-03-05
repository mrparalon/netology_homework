from datetime import datetime
import os


def logger(log_path):
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    def logger_decorator(function_to_log):
        start_time = datetime.now()
        def new_func(*args, **kwargs):
            with open(os.path.join(log_path, 'logs.txt'), 'a', encoding='utf8') as f:
                func_name = function_to_log.__name__
                func_return = function_to_log(*args, **kwargs)
                f.write(f"{start_time} FUNCTION {func_name} RETURNED {func_return}\n")
            return func_return
        return new_func
    return logger_decorator
