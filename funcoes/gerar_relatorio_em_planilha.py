import numpy as np
import pandas as pd
import pickle as pkl

"""
    Se for depurar a partir do PyCharm, as linhas abaixo deve substituida por:
    
    from fbr import fbr
"""
from funcoes import fbr
from funcoes.fbr import fbr_descricao

# # Ler os objetos:
# [endereco,
#  nome_das_variaveis,
#  nome_da_functus,
#  num_da_funcao,
#  C,
#  sigma,
#  VS,
#  R_quadrado,
#  tipo_da_saida] = pkl.load(open("../pickles/objetos_rep.pkl", "rb"))

# -*- coding: utf-8 -*-

def colocar_funcao(funcao,
                   i,
                   sigma,
                   VS,
                   C_texto,
                   planilha_solucao):

    """
    Esta função escreve na planilha solução a Função de
    Base Radial (FBR) escolhida para executar o Radial
    Basis Function (RBF), no estilo do Excel.

    :param funcao: Obrigatório. int.
        Função de base radial escolhida:
        1 - M: Multiquadrática;
        2 - MR: Multiquadrática Recíproca;
        3 - MRI: Multiquadrática Recíproca Inversa;
        4 - G: Gaussiana;
        5 - SH: Secante Hiperbólica;
        6 - CH: Cosseno Hiperbólico;
        7 - SPF: Splines de Placas Finas.
    :param i: Obrigatório. int.
        Último valor do contador i gerado no for fora desta função.
    :param sigma: Obrigatório. float.
        Desvio-padrão.
    :param VS: Obrigatório. array.
        Vector com o valor das sinapses (VS).
    :param C_texto: Obrigatório. array.
        Vector da coordenada dos polos no estilo do Excel, por exemplo,
        {x_um, x_dois_, x_tres}.
    :param planilha_solucao: Obrigatório. array.
        Planilha da solução com os valores das sinapses.
    :return: Planilha em Excel com a solução.
    """

    if funcao == 1:  # M: Multiquadrática
        formula = r"=SQRT((SQRT(" + \
                  r"SUMXMY2(Formulario" + \
                  r"!$B$2:$B" + str(len(VS)) + r"," + \
                  C_texto[i] + r"))) ^ 2 + " + \
                  str(sigma ** 2) + r")"
    elif funcao == 2:  # MR: Multiquadrática Inversa
        formula = r"=(1) / SQRT(" + \
                  r"(SQRT(SUMXMY2(" + r"Formulario" + \
                  r"!$B$2:$B" + str(len(VS)) + r"," + \
                  C_texto[i] + r"))) ^ 2 + " + \
                  str(sigma ** 2) + r")"
    elif funcao == 3:  # MRI: Multiquadrática Recíproca Inversa
        formula = r"=(1 / " + str(sigma) + r")" + \
        r"-(1) / SQRT((" + r"SQRT(" + r"SUMXMY2(Formulario" + \
        r"!$B$2:$B" + str(len(VS)) + r"," + C_texto[i] + \
        r"))) ^ 2 + " + str(sigma ** 2) + r")"
    elif funcao == 4:  # G: Gaussiana
        formula = r"=EXP(((-1) / (2 * " + str(sigma ** 2) + \
        r"))" + r" * (SQRT(SUMXMY2(" + r"Formulario!" + \
        r"$B$2:$B$" + str(len(VS)) + r"," + C_texto[i] + \
        r"))) ^ 2)"
    elif funcao == 5:  # SH: Secante Hiperbólica
        formula = r"=(1 / 2) * ((EXP(" + r"SQRT(" + \
        str(sigma ** 2) + r")) * (SQRT(" + "SUMXMY2(" + \
        r"Formulario!" + r"$B$2:$B$" + str(len(VS))  + \
        r"," + C_texto[i] + r"))))" + r" + EXP(-(SQRT(" + \
        str(sigma ** 2) + r")) * (SQRT(" + "SUMXMY2(" + \
        r"Formulario!" + r"$B$2:$B$" + \
        str(len(VS)) + r"," + C_texto[i] + r")))))"
    elif funcao == 6:  # CH: Cosseno Hiperbólico
        formula = r"=(1 / 2) * ((EXP(" + r"SQRT(" + \
        str(sigma ** 2) + r")) * (SQRT(SUMXMY2(" + \
        r"Formulario!" + r"$B$2:$B$" + \
        str(len(VS)) + r"," + C_texto[i] + r"))))" + \
        r" + EXP(-(SQRT(" + str(sigma ** 2) + \
        r")) * (SQRT(" + r"SUMXMY2(" + r"Formulario!" + \
        r"$B$2:$B$" + str(len(VS)) + r"," + \
        C_texto[i] + r")))))"
    # elif funcao == 7: # SPF: Splines de Placas Finas
    # (Para o Lar): desenvolver a função SPF.

    return formula

def gerar_relatorio_em_planilha(endereco,
                                nome_das_variaveis,
                                nome_da_functus,
                                funcao,
                                C,
                                sigma,
                                VS,
                                R_quadrado,
                                tipo_da_saida):

    """
    Esta função gera o relatório em planilha.

    :param endereco: Obrigatório. str.
        Endereço do banco de dados.
    :param nome_das_variaveis: Obrigatório. pd.DataFrame.
        Nome das variáveis.
    :param nome_da_functus: Obrigatório. str.
        Nome da função.
    :param funcao: Obrigatório. int.
        Função de base radial escolhida:
        1 - M: Multiquadrática;
        2 - MR: Multiquadrática Recíproca;
        3 - MRI: Multiquadrática Recíproca Inversa;
        4 - G: Gaussiana;
        5 - SH: Secante Hiperbólica;
        6 - CH: Cosseno Hiperbólico;
        7 - SPF: Splines de Placas Finas.
    :param C: Obrigatório. pd.DataFrame.
        Matrix com os Vectors de Coordenada dos Polos.
    :param sigma: Obrigatório. float.
        Desvio-padrão.
    :param VS: Obrigatório. pd.DataFrame.
        Vector com o valor das sinapses.
    :param R_quadrado: Obrigatório. float.
        Coeficiente de Acerto/Determinação/Estatístico R ** 2.
    :param tipo_da_saida: Obrigatório. str.
        Tipo de saída dos dados (int, float ou bool) da função experimental.
    :return Relatório em planilha.
    """

    # Criar um exportador Pandas Excel usando o XlsxWriter
    # como engine

    """
    Se for depurar a partir do PyCharm, a linha abaixo deve substituida por:
    
    endereco = "../saidas/" \
               + "formulario_" \
               + endereco \
               + ".xlsx"
    """

    endereco = "saidas/" \
               + "formulario_" \
               + endereco.replace("/", "_") \
               + ".xlsx"
    pasta_de_trabalho = \
        pd.ExcelWriter(endereco,
                       engine = "xlsxwriter")

    # nome_dos_VSs: Nome do valor das sinapses VS,
    # lembrar que o nome do último "VS" deve ser "b":
    nome_dos_VSs = []
    for i in range(0, len(VS), 1):
        if i != len(VS) - 1:
            nome_dos_VSs.append("VS[" + str(i) + "]")
        elif i == len(VS) - 1:
            nome_dos_VSs.append("b")

    solucao = pd.DataFrame(VS,
                           index = nome_dos_VSs,
                           columns = ["Valor"])

    # Converter o DataFrame em um objeto Excel
    solucao.to_excel(pasta_de_trabalho,
                     sheet_name = "Solucao")

    # Retornar um xlsxwriter objeto a partir de uma
    # pd.DataFrame. Perceber que, a variável
    # "pasta_de_trabalho" agora, trata-se
    # de uma estrutura do pacote "xlsxwriter".
    # pt_do_xlw: pasta de trabalho do Excel (workbook)
    pt_do_xlw = pasta_de_trabalho.book
    planilha_solucao = pasta_de_trabalho.sheets["Solucao"]

    planilha_solucao.write("A1", "Descrição")
    planilha_solucao.write("C1", "Função de Base Radial (FBR)")

    planilha_formulario = \
        pt_do_xlw.add_worksheet("Formulario")

    """
    Converter uma list em dict com os elementos da list
    na dict e as keys sendo enumeradas com os índices
    iniciando de 0, por exemplo, a posição do elemento
    da list
    """
    # C_texto: vector da coordenada dos polos no estilo do
    # Excel, por exemplo, {x_um, x_dois_, x_tres}.
    C_texto = []
    for i in range(0, len(C[0]), 1):
        texto = ""
        for j in range(0, len(C[0]), 1):
            if j == 0:
                texto = "{" + str(C[i, j])
            elif j != len(C[0]) - 1:
                # Perceber que, o separador de elementos
                # de um vector é ";".
                texto = texto + "; " + str(C[i, j])
            elif j == len(C[0]) - 1:
                texto = texto + "; " + str(C[i, j]) + "}"
        C_texto.append(texto)

    for i in range(0, len(VS), 1):
        if i != len(VS) - 1:
            planilha_solucao.write_formula("C" + str(i + 2),
                                           colocar_funcao(funcao,
                                                              i,
                                                              sigma,
                                                              VS,
                                                              C_texto,
                                                              planilha_solucao))

        if i == len(VS) - 1:
            planilha_solucao.write("C" + str(i + 2), 1)

    planilha_formulario.write("A1", "Descrição")
    planilha_formulario.write("B1", "Valor")
    for i in range(0, len(nome_das_variaveis), 1):
        planilha_formulario.write("A" + str(i + 2),
                                  nome_das_variaveis[i])

    # Functus Teórica:
    planilha_formulario.write("A" + str(i + 2 + 1),
                              nome_da_functus)
    planilha_formulario.write_formula("B" + str(i + 2 + 1),
                                      "=IFERROR(SUMPRODUCT(" +
                                      "\'" + "Solucao" +
                                      "\'" + "!$B$2" +
                                      ":$B$" + str(len(VS) + 1)
                                      + "," + "\'" + "Solucao"
                                      + "\'" + "!$C$2" +
                                      ":$C$" + str(len(VS) + 1)
                                      + "), \"\")")

    planilha_formulario.write("A" + str(i + 2 + 2),
                              "Coeficiente de acerto "
                              "(R ^ 2)")
    planilha_formulario.write("B" + str(i + 2 + 2),
                              R_quadrado)

    planilha_formulario.write("A" + str(i + 2 + 3),
                              "Função de Base Radial (FBR)")
    descricao = fbr_descricao(funcao)
    planilha_formulario.write("B" + str(i + 2 + 3),
                              descricao)
    planilha_formulario.write("A" + str(i + 2 + 4),
                              "Tipo de saída")
    planilha_formulario.write("B" + str(i + 2 + 4),
                              tipo_da_saida)

    # Formatar Formulario:
    # (Para o Lar)

    # Fechar o exportador Pandas Excel e imprimir o arquivo
    # Excel. NÃO esquecer de manter a planilha fechada
    # quando for executar este código.
    pasta_de_trabalho.save()

# print(gerar_relatorio_em_planilha(endereco,
#                                   nome_das_variaveis,
#                                   nome_da_functus,
#                                   num_da_funcao,
#                                   C,
#                                   sigma,
#                                   VS,
#                                   R_quadrado,
#                                   tipo_da_saida))