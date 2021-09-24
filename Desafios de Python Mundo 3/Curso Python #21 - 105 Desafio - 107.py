def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = dict()
    boletim['total'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['media'] = sum(nota) / len(nota)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim

resp = notas(5.5, 9.5, 10, 6.5)
#resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

help(notas)
