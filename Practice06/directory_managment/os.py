"""
OS Methods
Method	                        Description
os._exit()	                    Exits the process with the specified status
os.abort()	                    Terminates a running process immediately
os.access()	                    Uses the real uid/gid to check access to a path
os.add_dll_directory()	        Adds a path to the DLL search path
os.chdir()	                    Change the current working directory
os.chflags()	                Sets the flags of path to the numeric flags
os.chmod()	                    Changes the mode of path to the numeric mode
os.chown()	                    Changes the owner and group id of a specified path to the specified numeric owner id and group id
os.chroot()	                    Changes the root directory of the current process to a specified path
os.close()	                    Closes the specified file descriptor
os.closerange()	                Closes all file descriptors from fd_low to fd_high
os.confstr()	                Returns string-valued system configuration values
os.cpu_count()	                Returns the number of CPUs present in the system
os.ctermid()	                Returns the filename associated with the controlling terminal of the process
os.device_encoding()	        Returns the encoding of the device associated with the file descriptor, if it is connected to a terminal
os.dup()	                    Duplicates a file descriptor
os.dup2()	                    Duplicates a file descriptor to a given value
os.fchdir()	                    Changes the current working directory to a directory opened by os.open()
os.fchmod()	                    Changes the mode of a file to the specified numeric mode
os.fchown()	                    Changes the owner and group id of a file to the numeric uid and gid
os.fdatasync()	                Forces write of file to disc - not forces update of metadata
os.fdopen()	                    Returns an open file object connected to a file
os.fork()	                    Forks a child process
os.forkpty()	                Forks a child process, using a new pseudo-terminal as the child's controlling terminal
os.fpathconf()	                Returns system configuration information relevant to an open file
os.fsdecode()	                Decodes a file path
os.fsencode()	                Encodes a file path
os.fspath()	                    Returns the file system representation of a path
os.fstat()	                    Returns the status of a file
os.fstatvfs()	                Returns information about the file system of a file
os.fsync()	                    Forces write of file with file descriptor fd to disk
os.ftruncate()	                Truncates a file to a specified length
os.fwalk()	 
os.get_blocking()	            Returns the blocking mode information of the file descriptor
os.get_exec_path()	            Returns a list of directories, in which the system looks for named executable programs
os.get_handle_inheritable()	 
os.get_inheritable()	        Returns the inheritable flag of the file descriptor
os.get_terminal_size()	        Returns the size of a terminal as a pair of columns and lines
os.getcwd()	                    Returns the current working directory
os.getcwdb()	                Returns the current working directory in bytestring
os.getegid()	                Return the effective group id of the current process
os.getenv()	                    Returns the value of the environment variable key
os.getenvb()	                Returns the value of the environment variable key, in bytes
os.geteuid()	                Returns the effective user id of the current process
os.getgid()	                    Returns the real group id of the current process
os.getgrouplist()	            Returns a list of all group ids for a specified user
os.getgroups()	                Returns a list of supplementary group ids associated with the current process
os.getloadavg()	                Returns the load average over the last 1, 5, and 15 minutes
os.getlogin()	                Returns the name of the user logged in to the terminal
os.getpgid()	                Returns the process group id of a specific process id
os.getpgrp()	                Returns the current process group id
os.getpid()	                    Returns the process id of the current process
os.getppid()	                Returns the parent process id of the current process
os.getpriority()	            Returns the scheduling priority of a process, process group, or user
os.getresgid()	                Returns the current process' real, effective, and saved group ids
os.getresuid()	                Returns the current process' real, effective, and saved user ids
os.getsid()	                    Returns the session id of a process
os.getuid()	                    Returns the current process' real user id
os.initgroups()	                Initializes a group access list showing all the member groups of a user plus the group id
os.isatty()	                    Returns whether a file descriptor is open and connected to a tty(-like) device or not.
os.kill()	                    Sends a signal to the process with the specified process id
os.killpg()	                    Sends a signal to the process with the specified process id
os.lchflags()	                Changes the flags of a path to the numeric flags
os.lchmod()	                    Changes the mode of path to the numeric mode
os.lchown()	                    Changes the owner and group id of path to the numeric uid and gid
os.link()	                    Creates a hard link pointing to source named destination
os.listdir()	                Returns a list of the names of the entries in a directory
os.lockf()	                    Applies, tests, or removes a POSIX lock on an open file
os.lseek()	                    Sets the current position of file descriptor to the defined position
os.lstat()	                    Returns the status of a file or file descriptor, but does not follow symbolic links
os.major()	                    Returns the device major number from raw device number
os.makedev()	                Returns a raw device number from the specified major and minor device numbers
os.makedirs()	                Creates a directory recursively
os.memfd_create()	            Create an anonymous file and returns a file descriptor
os.minor()	                    Returns the device minor number from raw device number
os.mkdir()	                    Creates a directory (with a specified mode)
os.mkfifo()	                    Creates a FIFO named path (with a specified mode)
"""