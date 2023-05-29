'''MODULO DE GRAFICA'''
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./Imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('charts.png')
  plt.close()


if __name__ == '__main__':
  labels = ['A', 'B', 'C']
  values = 100, 196, 566
  generate_pie_chart(labels, values)
  