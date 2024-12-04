def max_profit_jobs(jobs):

    max_deadline = max(job[1] for job in jobs)
    time_slots = [None] * max_deadline  
    
    total_profit = 0 
    
    for profit, deadline in jobs:
  
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if time_slots[slot] is None:
                time_slots[slot] = (profit, deadline)  
                total_profit += profit  
                break  
    
    return total_profit


jobs = [(20, 2), (15, 2), (10, 1), (5, 3), (1, 3)]  
result = max_profit_jobs(jobs)
print(f"Maximum profit: {result}")
