from time import sleep
from function import beam
from table import plot


beam = beam(12, 6, 0.16)
data = beam.read_data()
for i in range((data.shape[0]+1)):
# for i in range(3):
    q = beam.q_calculation(data, i)
    sumQ = beam.R_calculation(q)
    list_M = beam.M_calculation(sumQ, q)
    list_F = beam.F_calculation(sumQ, q)
    sleep(0.1)


# plot(list_M)

