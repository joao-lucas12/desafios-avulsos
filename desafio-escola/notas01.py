 # Média escolar
p1 = float(input('primeira prova: ')) #Use um float para utilizar números flutuantes
p2 = float(input('segunda prova: ')) #O int é só para números inteiros

id = float(input('teste semanal'))
s = p1 + p2 + id 
print('primeira prova {:.1f}, segunda prova {:.2f}, teste semanal {:.3f}média {:.4f}'.format(p1, p2, id, s/3))