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
