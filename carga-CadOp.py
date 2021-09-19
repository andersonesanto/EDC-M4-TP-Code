import pandas as pd
import tabulate

CadOpUrl = "http://ftp.dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"

dfCadOp = pd.read_csv(CadOpUrl,
                      sep=";", encoding="LATIN1")

isPE = dfCadOp['UF'] == 'PE'
dfCadOpPE = dfCadOp[isPE]
print('dadosabertos.ans.gov.br - cadastro de operadoras de plano de saúde ativas em Pernambuco')
print('Quantidade de planos de saúde privados em Pernambuco: {}'.format(
    len(dfCadOpPE.index)))
print(dfCadOpPE[['Registro_ANS', 'Razao_Social']])
