#1. No

#2. Time-Efficiency and Dependency Management

#3.
import numpy as np
import scipy as sp
dir(np)
dir(sp)

#4.
import scipy
scipy.func
#or
from scipy import func
func

#5. List object does not have sum method

#6.
arr = [1, 2, 3]
[print(i) for i in arr]

#7. There is no module np and false, true are not keywords in python

#8. Test whether the skew is different from the normal distribution.
from scipy.stats import skewtest
skewtest([1, 2, 3, 4, 5, 6, 7, 8])

#9. Arithmetic mean is the average of all the numbers while geometric mean is the average change in those numbers.

#10.
import numpy as np
ret=np.array([0.05,0.11,-0.03])
pow(np.prod(ret+1),1./len(ret))-1

#11.
import numpy as np
ret = [0.1, 0.02, 0.43, -0.07]
np.mean(ret)
pow(np.prod(ret+1), 1./len(ret)) - 1

#12. It's the measure of how many stds the value is away from the mean.
import numpy as np
a = np.array([ 0.7972,  0.0767,  0.4383,  0.7866,  0.8091,
               0.1954,  0.6307,  0.6599,  0.1065,  0.0508])
from scipy import stats
stats.zscore(a)

#13. It should be iterable as it represents the cash flows.

#14. Some modules depend on other modules and we call it dependency. The package managers such as pip deal with this.

#15. It's time efficient as someone already solved the problem you are dealing with. But the problem is that it adds addiitional complexity as your program depends on that module.

#16.
import numpy_financial as nf
nf.pv(0.1, 4, 0, 100)
nf.fv(0.1, 4, 0, 100)

#17. No

#18. ---

#19. We can do "help()" then "modules" or in python module docs

#20. We can do "help()" then "modules finance"

