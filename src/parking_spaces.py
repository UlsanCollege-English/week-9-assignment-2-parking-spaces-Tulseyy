"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""

def min_parking_spots(intervals):
    # Handle empty input
    if not intervals:
        return 0
        
    # Sort intervals by start time for chronological processing
    intervals.sort(key=lambda x: x[0])
    
    # Initialize min heap to track end times
    import heapq
    end_times = []
    max_spots = 0
    
    # Process each interval
    for start, end in intervals:
        # Remove all spots that can be reused (end time <= current start)
        while end_times and end_times[0] <= start:
            heapq.heappop(end_times)
            
        # Add current interval's end time
        heapq.heappush(end_times, end)
        
        # Update maximum spots needed (current heap size = spots in use)
        max_spots = max(max_spots, len(end_times))
    
    return max_spots
