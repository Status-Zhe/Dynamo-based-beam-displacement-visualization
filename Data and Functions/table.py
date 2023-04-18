import pandas as pd
import matplotlib.pyplot as plt

def plot(M_list):
    data = pd.read_excel('StaticStrain_Displacement.xlsx', sheet_name='Sheet1')
    Displacement = data['Displacement(m)']
    # print(Strain.values)
    plt.plot(Displacement.values)
    plt.plot(range(1, 13), M_list, label='-r')
    plt.scatter(range(13), Displacement.values, s=50)
    plt.scatter(range(1, 13), M_list, s=50)
    plt.xlabel('Sensor Locations')
    plt.ylabel('Strain(a)')
    plt.legend(
        [ 'Actual', 'Virtual'], loc='lower right', fancybox=True, framealpha=1, shadow=True, borderpad=True
    )
    plt.show()