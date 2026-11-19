from __future__ import annotations
from typing import List, Sequence
import time 
from collections import deque 
from typing import List, Sequence 
def chech_window(window, n):
    if window <= 0 or window > n:
        raise ValueError("Размер окна должен быть в пределах от 1 до len(n)")
def simple_moving_average(data, window):
    for i in range(len(data) - window + 1): 
     result.append(sum(data[i:i+window]) / window)
    running = sum(data[:window]) 
    result = [running / window] 
    for i in range(window, len(data)): 
     running += data[i] - data[i - window] 
     result.append(running / window)
    return result
def check_window(window: int, n: int) -> None:
    if n <= 0:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    if isinstance(window, bool) or not isinstance(window, int) or window < 1:
        raise ValueError(f"window должно быть целым числом >= 1 (получено: {window!r})")
    if window > n:
        raise ValueError(f"window ({window}) не может превышать длину ряда ({n})")
def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    check_window(window, len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result
def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Для центрированной скользящей средней окно должно быть нечётным (получено: {window})"
        )
    return simple_moving_average(data, window)
def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if isinstance(alpha, bool) or not isinstance(alpha, (int, float)) or not (0 < alpha <= 1):
        raise ValueError(f"alpha должно быть в диапазоне (0, 1] (получено: {alpha!r})")
    result: List[float] = [float(data[0])]
    for x in data[1:]:
        ema_prev = result[-1]
        result.append(alpha * x + (1.0 - alpha) * ema_prev)
    return result
def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:  
    check_window(window, len(data)) 
    result = [] 
    d = deque() 
    running_sum = 0.0 
    for x in data: 
        d.append(x) 
        running_sum += x 
        if len(d) > window: 
            running_sum -= d.popleft() 
        if len(d) == window: 
            result.append(running_sum / window) 
    return result 
def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict: 
    check_window(window, len(data)) 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average(data, window) 
    t_list = (time.perf_counter() - t0) / repeats 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average_deque(data, window) 
    t_deque = (time.perf_counter() - t0) / repeats 
    return {"list": t_list, "deque": t_deque} 