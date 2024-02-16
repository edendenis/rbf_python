import numpy as np
import pickle as pkl

# # Ler os objetos:
# [num_da_funcao,
#  variaveis,
#  C,
#  sigma] = pkl.load(open("../pickles/objetos_matrix_R.pkl", "rb"))

def fbr(num_da_funcao,
        X,
        C,
        sigma):

    """
    Esta função retorna o cálculo da Função de Base Radial (FBR).

    :param num_da_funcao: Obrigatório. int.
        Função de base radial escolhida:
        1 - M: Multiquadrática;
        2 - MR: Multiquadrática Recíproca;
        3 - MRI: Multiquadrática Recíproca Inversa;
        4 - G: Gaussiana;
        5 - SH: Secante Hiperbólica;
        6 - CH: Cosseno Hiperbólico;
        7 - SPF: Splines de Placas Finas.
    :param X: Obrigatório. array.
        Matrix X de variáveis.
    :param C: Obrigatório. array.
        Matrix C de coordenada do polos.
    :param sigma: Obrigatório. float.
        Desvio-padrão.
    :return: Cálculo.
    """

    # OBSERVAÇÃO(ÕES): caso adicione alguma função, NÃO esquecer de
    # adicionar a descrição na function fbr_descricao.

    # k: constante dependente de sigma
    k = 1 / (2 * sigma ** 2)

    if num_da_funcao == 1: # M: Multiquadrática
        calculo = np.sqrt((np.linalg.norm(X - C)) ** 2 +
                          (1 / k) ** 2)
    elif num_da_funcao == 2: # MR: Multiquadrática Recíproca
        calculo = 1 / (np.sqrt((np.linalg.norm(X - C)) ** 2 +
                          (1 / k) ** 2))
    elif num_da_funcao == 3: # MRI: Multiquadrática Recíproca Inversa
        calculo = 1 / (1 / k) - \
                  1 / np.sqrt((np.linalg.norm(X - C)) ** 2 +
                          (1 / k) ** 2)
    elif num_da_funcao == 4: # G: Gaussiana
        calculo = np.exp(- k * (np.linalg.norm(X - C)) ** 2)
    elif num_da_funcao == 5: # SH: Secante Hiperbólica
        calculo = 2 / \
                  (np.exp(k * (np.linalg.norm(X - C)) ** 2) +
                   np.exp(- k * (np.linalg.norm(X - C)) ** 2))
    elif num_da_funcao == 6: # CH: Cosseno Hiperbólico
        calculo = (np.exp((1 / (2 * sigma ** 2))
                         * (np.linalg.norm(X - C)) ** 2) +
                   np.exp((-1 / (2 * sigma ** 2))
                          * (np.linalg.norm(X - C)) ** 2)) / 2
    elif num_da_funcao == 7: # SPF: Splines de Placas Finas
        # lim_inf = Limite inferior
        lim_inf = 0
        # lim_sup = Limite superior
        lim_sup = 10
        global b

        np.random.seed(42)

        b = np.random.randint(lim_inf, lim_sup)
        calculo = np.linalg.norm(X - C) ** (2 * b) * \
                  np.log(np.linalg.norm(X - C))

    return calculo

def fbr_descricao(num_da_funcao):

    """
    Esta função retorna a descrição da Função de Base Radial (FBR).

    :param num_da_funcao: Obrigatório. int.
        Função de base radial escolhida:
        1 - M: Multiquadrática;
        2 - MR: Multiquadrática Recíproca;
        3 - MRI: Multiquadrática Recíproca Inversa;
        4 - G: Gaussiana;
        5 - SH: Secante Hiperbólica;
        6 - CH: Cosseno Hiperbólico;
        7 - SPF: Splines de Placas Finas.
    :return: descricao.
    """

    if num_da_funcao == 1: # M: Multiquadrática
        descricao = "Multiquadrática (M)"
    elif num_da_funcao == 2: # MR: Multiquadrática Recíproca
        descricao = "Multiquadrática Recíproca (MR)"
    elif num_da_funcao == 3: # MRI: Multiquadrática Recíproca Inversa
        descricao = "Multiquadrática Recíproca Inversa (MRI)"
    elif num_da_funcao == 4: # G: Gaussiana
        descricao = "Gaussiana (G)"
    elif num_da_funcao == 5: # SH: Secante Hiperbólica
        descricao =  "Secante Hiperbólica (SH)"
    elif num_da_funcao == 6: # CH: Cosseno Hiperbólico
        descricao =  "Cosseno Hiperbólico (CH)"
    elif num_da_funcao == 7: # SPF: Splines de Placas Finas
        descricao =  "Splines de Placas Finas (SPF)"

    return descricao

# print(fbr_descricao(num_da_funcao))
# print(fbr(num_da_funcao,
#           variaveis[1],
#           C[0],
#           sigma))