import os
import pandas as pd
import geopandas as god
import matplotlib.pyplot as plt

l = []
for i in range(0,191,5):
    l.append(i)

list_of_years = []
s = god.read_file("POL_adm1.shp")

for i in l:
    data = pd.read_csv(r'C:\Users\PC\PycharmProjects\GSCA\all_files\file{0}.csv'.format(i))
    new_data = s.merge(data, on='ID_1')
    s = new_data
    list_of_years.append('infected{0}'.format(i))


def obraz(list_of_years):

    output_path = 'charts'
    vmin, vmax = 0, 15000

    for year in list_of_years:


        # create map, UDPATE: added plt.Normalize to keep the legend range the same for all maps
        fig = new_data.plot(column=year, cmap='OrRd', figsize=(6.4, 4.8), linewidth=1.0,  edgecolors='dimgrey', vmin=vmin,
                            vmax=vmax,
                            legend=True, legend_kwds={'label': "Infected population  "}, norm=plt.Normalize(vmin=vmin, vmax=vmax))
        fig.axis('off')
        fig.set_title('Spread of disease in Poland', \
                      fontdict={'fontsize': '20',
                                'fontweight': '3'
                                ,'color':'white'})
        only_year = year[8:]
        fig.annotate('      Day: '+only_year,
                     xy=(0.1, .225), xycoords='figure fraction',
                     horizontalalignment='left', verticalalignment='top',
                     fontsize=15)

        filepath = os.path.join(output_path, only_year + '_disease.png')
        chart = fig.get_figure()
        chart.savefig(filepath, dpi=300)



    return "finish"

obraz(list_of_years)