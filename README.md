Python Port Scanner

​A custom TCP port scanner built with Python for network reconnaissance and auditing.
​Features and Technical Details:
​Target Requirements: Allows the user to specify a target IP address alongside a custom port range (Start and End ports) for targeted auditing.
​Socket Programming: Utilizes Python's built-in socket library (AF_INET for IPv4 and SOCK_STREAM for TCP connections) to establish network communication.
​Efficient Scanning Logic: Implements a for loop to iterate through the specified port range, utilizing connect_ex() instead of the standard connect() to cleanly return error codes rather than crashing when a port is closed.
​Error Handling: Wrapped in try-except blocks to gracefully handle user interruptions using KeyboardInterrupt (Ctrl+C), and catches network resolution errors (socket.gaierror) to prevent ugly traceback messages if an invalid host is entered.
​Execution Timing: Integrates the datetime library to track the start time and measure the total execution duration of the scan.
