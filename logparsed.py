import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


log_file_path = r"out_without_val.txt"
regex = ''

match_list = []
match_list2 = []
with open(log_file_path, "r") as file:
    for line in file:
        a = line.split()
        if len(a) > 1:
            # if a[0]=='32/25000':
            #     match_list.append(a[10])
            if a[0]=='24992/25000':
                match_list.append(a[10])

            if a[0]=='25000/25000':
                match_list2.append(a[16])

print(match_list)

# red dashes, blue squares and green triangles
plt.plot(match_list, 'r--', match_list2, 'bs')
plt.savefig('acuracy and lost')
# plt.plot(match_list)
# plt.ylabel('some numbers')
# plt.show()
