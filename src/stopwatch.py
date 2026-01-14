# ============================================================
# Stopwatch Module
# ============================================================
# 
# Add your stopwatch functionality here!
#
# ============================================================

class Stopwatch:
    """Stopwatch functionality for timing events."""
    
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.laps = []
    
    def start(self):
        """Start the stopwatch."""
        pass
    
    def stop(self):
        """Stop/pause the stopwatch."""
        pass
    
    def reset(self):
        """Reset the stopwatch."""
        pass
    
    def lap(self):
        """Record a lap time."""
        pass
    
    def get_elapsed(self):
        """Get elapsed time."""
        pass
