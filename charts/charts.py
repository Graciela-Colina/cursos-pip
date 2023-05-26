import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['Ana', 'Bianca', 'Caroline']
    values = [200, 34, 111]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close

