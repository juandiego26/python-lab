from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
from sympy import FiniteSet

# print(dir(plt))
A = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
B = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19, 8)

plt.figure(figsize=(10, 8))
v = venn2(subsets=[A, B], set_labels=('A', 'B'))
v.get_label_by_id('10').set_text(A - B)
v.get_label_by_id('11').set_text(A.intersection(B))
v.get_label_by_id('01').set_text(B - A)
c = venn2_circles(subsets=[A, B], linestyle='dashed')
c[0].set_ls('solid')
plt.show()