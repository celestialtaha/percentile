# percentile
With this python library you can compute and display progress in loops that take long time to complete.

# Usage
## import
from Percentile import Progress
## create instance
first parameter is range or the number of iterations,second is updating step.
for example below code creates an instance with 12000 iterations .the progress is updated every 5% and displayed graphically.
also if you specify cls = false it doesn't clear at each update.

prog = Progress(12000, 5, cls = True)

## compute and display progress
for i in range(12000):

	# do something
  
	prog.compute(i)

# Output
|------------------  | 90.0 %
