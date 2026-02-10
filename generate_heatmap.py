import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

CN_FONT = 'Hiragino Sans GB'
plt.rcParams['font.family'] = [CN_FONT, 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Data
data = np.array([
    [10, 20, 60, 10],   # H (Happiness)
    [15, 50, 25, 10],   # E (Engagement)
    [60, 20, 10, 10],   # A (Adoption)
    [20, 15, 25, 40],   # R (Retention)
    [30, 20, 30, 20],   # T (Task Success)
])

row_labels = [
    'H（Happiness）',
    'E（Engagement）',
    'A（Adoption）',
    'R（Retention）',
    'T（Task Success）',
]
col_labels = ['引入期', '成长期', '成熟期', '衰退期']

# Blue colormap (light → deep blue, no black/purple)
cmap = mcolors.LinearSegmentedColormap.from_list(
    'custom_blue',
    ['#EBF2FF', '#C5D8FF', '#7AADFF', '#3B82F6', '#1D4ED8', '#1E40AF'],
    N=256,
)

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('white')

sns.heatmap(
    data,
    annot=True,
    fmt='d',
    cmap=cmap,
    vmin=0,
    vmax=60,
    linewidths=2,
    linecolor='white',
    xticklabels=col_labels,
    yticklabels=row_labels,
    annot_kws={'size': 16, 'weight': 'bold'},
    cbar_kws={'label': '权重（%）', 'shrink': 0.85},
    ax=ax,
)

# Title
ax.set_title('HEART权重分布矩阵（按生命周期）', fontsize=18, fontweight='bold',
             pad=20, color='#111827')

# Axis labels
ax.set_xlabel('用户生命周期', fontsize=13, labelpad=12, color='#374151')
ax.set_ylabel('HEART 维度', fontsize=13, labelpad=12, color='#374151')

# Tick styling
ax.tick_params(axis='x', labelsize=12, colors='#374151', length=0)
ax.tick_params(axis='y', labelsize=12, colors='#374151', length=0, rotation=0)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Colorbar styling
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=10, colors='#6B7280')
cbar.set_ticks([0, 10, 20, 30, 40, 50, 60])
cbar.outline.set_visible(False)

plt.tight_layout()
plt.savefig(
    '/Users/kay_sensei/Documents/kay_workplace/resume-portfolio/images/1_heart_heatmap.png',
    dpi=200,
    bbox_inches='tight',
    facecolor='white',
    edgecolor='none',
)
plt.close()
print('Done!')
