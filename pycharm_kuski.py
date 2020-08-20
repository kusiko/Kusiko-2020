# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
df = pd.read_excel(r'C:\for copy\Downloads\Live, Core, Lite Buildings - US Office - Usage Metrics SSAS.xlsx', sheet_name='cancellations')
import matplotlib.pyplot as plt
to_graph = df['Property Type Name'].value_counts()
to_graph.plot(kind='bar', color='blue')
plt.title('Property Type by FacID Count', fontsize=11)
plt.xlabel('Building Type')
plt.ylabel('# of FacIDs')
newfiletocommit = 'this is new'