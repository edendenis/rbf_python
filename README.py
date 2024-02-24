#!/usr/bin/env python
# coding: utf-8

# <!-- ESCUDOS DO PROJETO -->
# <p align="center">
#   <img src="https://img.shields.io/github/contributors/edendenis/rbf_python.svg?style=flat-square" alt="Contribuidores">
#   <img src="https://img.shields.io/github/forks/edendenis/rbf_python.svg?style=flat-square" alt="Forks">
#   <img src="https://img.shields.io/github/stars/edendenis/rbf_python.svg?style=flat-square" alt="Estrelas">
#   <img src="https://img.shields.io/github/issues/edendenis/rbf_python.svg?style=flat-square" alt="Issues">
#   <img src="https://img.shields.io/github/license/edendenis/rbf_python.svg?style=flat-square" alt="Licença MIT">
#   <a href="https://www.linkedin.com/in/seu_linkedin"><img src="https://img.shields.io/badge/-LinkedIn-blue.svg?style=flat-square&logo=linkedin&colorB=555" alt="LinkedIn"></a>
# </p>
# 

# <!-- LOGOTIPO DO PROJETO -->
# <div style="display: flex; justify-content: center;">
#    <a href="https://github.com/othneildrew/Best-README-Template">
#      <img src="figures/logotipo_edf_vetorizado_fundo_roxo_e_nome.png" alt="Logo" width="80" height="80">
#    </a>
# </div>
# 
# <h3 align="center">EDF Radial Basis Function (RBF) Python</h3>
# 
# <div style="display: flex; justify-content: center;">
#   <a href="https://zenodo.org/doi/10.5281/zenodo.10668855">
#     <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
#   </a>
# </div>
# 
# <p align="center">
#  Um modelo README incrível para impulsionar seus projetos!
#  <br />
#  <a href="https://github.com/edendenis/rfbnn"><strong>Explore os documentos »</strong></a>
#  <br />
#  <br />
#  <a href="https://github.com/edendenis/rfbnn">Ver demonstração</a>
#  ·
#  <a href="https://github.com/edendenis/rfbnn">Relatar bug</a>
#  ·
#  <a href="https://github.com/edendenis/rfbnn">Solicitar recurso</a>
# </p>
# 

# ## Resumo
# 
# Aplicação computacional de Redes Neurais de Função de Base Radial (RBFNN) eu empregam funções de base radial em camadas ocultas, modelando com eficiência relacionamentos não lineares complexos em dados. Sua arquitetura exclusiva permite aproximação, classificação e regressão precisas de funções, tornando-os versáteis e eficazes em vários domínios.
# 
# ## _Abstract_
# 
# _Computational Application of Radial Basis Function Neural Networks (RBFNN) I employ radial basis functions in hidden layers, efficiently modeling complex nonlinear relationships in data. Their unique architecture enables accurate function approximation, classification, and regression, making them versatile and effective across multiple domains._
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ## Revisão(ões)/Versão(ões)
# 
# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 15/09/2022      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</li></ul> |
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ### Construído com
# 
# Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.
# 
# * [![Python][Python]][https://www.python.org/]
# * [![Anaconda][Python]][https://www.anaconda.com/]
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- COMEÇANDO -->
# ## 1.1 Começando
# 
# Este é um exemplo de como você pode dar instruções sobre como configurar seu projeto localmente.
# Para obter uma cópia local instalada e funcionando, siga estas etapas simples de exemplo.
# 
# ### 1.2 Pré-requisitos
# 
# Este é um exemplo de como listar os itens necessários para usar o software e como instalá-los.
# * Python 3.8
# * Anaconda 24.1.0
# * Git
# * IDE para executar o arquivo `.ipynb`
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## 2. Guia de instalação
# 
# ### 2.1 Instalar o Git
# 
# Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads
# 
# Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### 2.2 Criar chave SSH para a conta do usuário [1]
# 
# #### 2.2.1 Verificar se foi liberado o acesso ao Git
# 
# Antes de seguir os passos de uma das Seções abaixo (Linux e/ou Windows), confirmar com um dos administradores do Git se foi liberado o acesso para a sua conta de e-mail. Se não, solicitar o acesso antes de prosseguir com o passo a passo de uma Seções abaix (Linux e/ou Windows). 
# 
# #### 2.2.2 `Linux`
# 
# Para gerar uma chave SSH no Linux Ubuntu, você pode seguir os passos abaixo:
# 
# 1. Abra um terminal no seu sistema Ubuntu. Você pode fazer isso pressionando "Ctrl + Alt + T" ou procurando por "Terminal" no menu de aplicativos.
# 
# 2. No terminal, digite o seguinte comando para gerar um novo par de chaves SSH: `ssh-keygen -t rsa`
# 
# 1. O comando acima irá gerar um par de chaves RSA. Você também pode usar outros algoritmos de chave, como `dsa` ou `ecdsa`, se preferir. Pressione Enter para aceitar o local padrão do arquivo da chave.
# 
# 2. Em seguida, você será solicitado a inserir uma frase secreta (passphrase) para proteger sua chave. É recomendável usar uma senha forte e exclusiva para aumentar a segurança. Você pode pressionar Enter para deixar a frase secreta em branco, mas isso diminuirá a segurança da sua chave.
# 
# 3. Após fornecer a frase secreta ou pressionar Enter, o comando `ssh-keygen` irá gerar duas chaves: uma chave privada (id_rsa) e uma chave pública (id_rsa.pub). A chave privada deve ser mantida em segredo e protegida com a frase secreta, enquanto a chave pública pode ser compartilhada.
# 
# 4. Por padrão, as chaves SSH são salvas no diretório `~/.ssh/`. Você pode listar o conteúdo desse diretório usando o comando: `ls ~/.ssh/`
# 
# 1. Agora você pode usar sua chave pública (id_rsa.pub) para autenticar em servidores remotos. Você pode copiar a chave pública para o servidor remoto usando o comando `ssh-copy-id`. Por exemplo: `ssh-copy-id -i ~/.ssh/id_rsa.pub usuário@servidor`
# 
# Substitua "usuário" pelo seu nome de usuário no servidor remoto e "servidor" pelo endereço IP ou nome do servidor remoto. Você será solicitado a inserir a senha do usuário no servidor remoto.
# 
# Depois de copiar a chave pública, você poderá fazer login no servidor remoto sem precisar digitar a senha toda vez, desde que a chave privada esteja presente no sistema local e a frase secreta (se fornecida) esteja correta.
# 
# Lembre-se de proteger sua chave privada e evitar compartilhá-la com outras pessoas. É recomendável usar autenticação por chave SSH em vez de senhas, pois oferece uma camada adicional de segurança.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### 2.3 Atualizar pacotes `pip` e `setuptools` [3]
# 
# É recomendado que sejam atualizado os pacotes, como segue:
# 
# 1. **Verificar a versão do `pip`:** Verifique se você está usando uma versão atualizada do `pip`. Execute o seguinte comando para atualizá-lo, caso necessário: `pip install --upgrade pip`
# 
# 2. **Verificar a versão do `setuptools`:** Verifique se você possui a versão mais recente do pacote `setuptools` instalada. Execute o seguinte comando para atualizá-lo, se necessário:`pip install --upgrade setuptools`
# 
# 3. **Verificar a versão do `wheel`:** O erro menciona que a opção `bdist_wheel` é inválida. Isso pode acontecer se o pacote `wheel` estiver desatualizado. Execute o seguinte comando para atualizar o pacote `wheel` com o comando: `pip install --upgrade wheel`
# 
# 4. É recomendado reiniciar o Sistema Operacional (SO).

# #### 2.2.3 `Windows` [2]
# 
# Para gerar uma chave SSH no Windows para uso no GitLab, você pode seguir as etapas abaixo:
# 
# 1. Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads
# 
# 2. Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.
# 
# 3. No Git Bash, digite o seguinte comando para gerar uma nova chave SSH `ssh-keygen -t rsa -C "seu_email@exemplo.com"` (`@gitlab.com`)
# 
# Certifique-se de substituir `seu_email@exemplo.com` pelo seu endereço de e-mail associado à sua conta do GitLab. Você pode deixar a senha em branco pressionando Enter duas vezes.
# 
# 4. Será solicitado que você forneça um local para salvar a chave. Você pode simplesmente pressionar Enter para aceitar o local padrão (geralmente `C:\Usuários\SeuNome.ssh\id_rsa`).
# 
# 5. O comando irá gerar a chave SSH pública e privada. Por padrão, a chave pública será salva como `id_rsa.pub`.
# 
# 6. Agora, você precisa adicionar a chave SSH pública à sua conta do GitLab. Abra o GitLab no seu navegador e faça login na sua conta.
# 
# 7. No canto superior direito da página, clique na sua foto de perfil e vá para `Settings` (Configurações) no menu suspenso.
# 
# 8. No menu lateral esquerdo, clique em `SSH Keys` (Chaves SSH).
# 
# 9. No campo 'Key', abra o arquivo `id_rsa.pub` (ou qualquer nome que você tenha dado à sua chave pública) que você gerou anteriormente. Copie todo o conteúdo do arquivo e cole no campo "Key" no GitLab.
# 
# 10. Dê um nome para a chave, por exemplo, `Meu Computador` e clique em `Add Key` (Adicionar chave).
# 
# Agora você gerou e adicionou com sucesso uma chave SSH para uso no GitLab. Você poderá usar essa chave para autenticar suas operações do GitLab usando o Git no Windows.
# 
# Depois de copiar a chave pública, você poderá fazer login no servidor remoto sem precisar digitar a senha toda vez, desde que a chave privada esteja presente no sistema local e a frase secreta (se fornecida) esteja correta.
# 
# Lembre-se de proteger sua chave privada e evitar compartilhá-la com outras pessoas. É recomendável usar autenticação por chave SSH em vez de senhas, pois oferece uma camada adicional de segurança.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### 2.3 Atualizar pacotes `pip` e `setuptools` [3]
# 
# É recomendado que sejam atualizado os pacotes, como segue:
# 
# 1. **Verificar a versão do `pip`:** Verifique se você está usando uma versão atualizada do `pip`. Execute o seguinte comando para atualizá-lo, caso necessário: `pip install --upgrade pip`
# 
# 2. **Verificar a versão do `setuptools`:** Verifique se você possui a versão mais recente do pacote `setuptools` instalada. Execute o seguinte comando para atualizá-lo, se necessário:`pip install --upgrade setuptools`
# 
# 3. **Verificar a versão do `wheel`:** O erro menciona que a opção `bdist_wheel` é inválida. Isso pode acontecer se o pacote `wheel` estiver desatualizado. Execute o seguinte comando para atualizar o pacote `wheel` com o comando: `pip install --upgrade wheel`
# 
# 4. É recomendado reiniciar o Sistema Operacional (SO).
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### 2.3 Atualizar pacotes `pip` e `setuptools` [3]
# 
# É recomendado que sejam atualizado os pacotes, como segue:
# 
# 1. **Verificar a versão do `pip`:** Verifique se você está usando uma versão atualizada do `pip`. Execute o seguinte comando para atualizá-lo, caso necessário: `pip install --upgrade pip`
# 
# 2. **Verificar a versão do `setuptools`:** Verifique se você possui a versão mais recente do pacote `setuptools` instalada. Execute o seguinte comando para atualizá-lo, se necessário:`pip install --upgrade setuptools`
# 
# 3. **Verificar a versão do `wheel`:** O erro menciona que a opção `bdist_wheel` é inválida. Isso pode acontecer se o pacote `wheel` estiver desatualizado. Execute o seguinte comando para atualizar o pacote `wheel` com o comando: `pip install --upgrade wheel`
# 
# 4. É recomendado reiniciar o Sistema Operacional (SO).

# ### 2.4 Clonar o repositório do Git e instalar o pacote `proplib`
# 
# #### 2.4.1 `Linux`
# 
# 1. **Clone o repositório:**
# 
#   - **Pelo terminal:** `git clone git@github.com:edendenis/rbf_python.git`
# 
#   - **(Ou) Fazer o _download_ do repositório `.zip` pela página web do GitHub, botão ao lado do botão azul `clone` à direita
# 
#   <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# #### 2.4.2 `Windows`
# 
# 1. **Clone o repositório:**
# 
#   - **Pelo terminal:** `git clone git@github.com:edendenis/rbf_python.git`
# 
#   - **(Ou) Fazer o _download_ do repositório `.zip` pela página web do GitHub, botão ao lado do botão azul `clone` à direita
# 
#   <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- COMO EXECUTAR A APLICAÇÂO -->
# ## 3. Como executar a aplicação
# 
# 
# Use este espaço para mostrar exemplos úteis de como um projeto pode ser usado. Capturas de tela adicionais, exemplos de código e demonstrações funcionam bem neste espaço. Você também pode vincular a mais recursos.
# 
# _Para mais exemplos, consulte a [Documentação](https://example.com)_
# 
# 1. Abrir o arquivo `main_<nome_da_aplicacao>.ipynb` o qual está com comentários, alterar o banco de dados (existem exemplos de bancos de dados) na pasta que deverá ser utilizado para a execução e executar todas as células. 
#     
#     Perceber que o <nome_da_aplicacao> trata-se, redudantemente, do nome da aplicação. Coloquei desta forma, pois quis, por ora, generalizar o arquivo `README.md` para poder criar o repositório de cada uma das aplicações que desenvolvi ao longo da minha carreira.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- ROTEIRO -->
# ## Roteiro
# 
# - [x] Adicionar registro de alterações
# - [x] Adicionar links de volta ao topo
# - [x] Adicionar modelos adicionais com exemplos
# - [x] Suporte multilíngue
#      - [x] Espanhol
#      - [x] Inglês
#      - [x] Português
#      - [x] Português brasileiro 
# 
# Consulte os [problemas abertos](https://github.com/edendenis/rbfnn/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- CONTRIBUIÇÔES -->
# ## Contribuições
# 
# As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.
# 
# Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a tag “aprimoramento”.
# Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!
# 
# 1. Bifurque o projeto
# 2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)
# 3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)
# 4. Envie para a filial (`git push origin feature/AmazingFeature`)
# 5. Abra uma solicitação pull
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- CONTATO -->
# ## Contato
# 
# Eden Denis F. da S. L. Santos - [LinkedIn](https://linkedin.com/in/eden-santos-51a826149/) - edendenis@gmail.com
# 
# Link do projeto: [https://github.com/edendenis/rfbnn](https://github.com/edendenis/rbf_python)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- ACKNOWLEDGMENTS -->
# ## Agradecimentos
# 
# * [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)
# * [Choose an Open Source License](https://choosealicense.com)
# * [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
# * [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
# * [Malven's Grid Cheatsheet](https://grid.malven.co/)
# * [Img Shields](https://shields.io)
# * [GitHub Pages](https://pages.github.com)
# * [Font Awesome](https://fontawesome.com)
# * [React Icons](https://react-icons.github.io/react-icons/search)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Referências
# 
# [1]	BROOMHEAD, D.; LOWE, D. Lowe. ***Multivariable functional interpolation and adaptive networks: complex systems***. .2, P. 321, 1988.  
# 
# [2] HEBB, D. O.. ***Brain mechanisms and learning***. London: J. F. Delafresnaye, 1961.
# 
# [3] MÁSSON, E.; WANG, Y.. ***Introduction to computation and learning in artificial neural networks***. European Journal of Operational Research, North-Holland, v. 47, 1990.
# 
# [4] HAYKIN, S.. ***Redes neurais: princípios e prática***. Tradução de Paulo Martins Engel. 2. ed. Porto Alegre: Bookman, 2001.
# 
# [5] BARONE, D. A. C.. ***Sociedades artificiais: a nova fronteira da inteligência nas máquinas***. Porto Alegre: Bookman, 2003.
# 
# [6] RICIERI, A. P.; SANTOS, E. D. F. da S. L.. ***Radial basis function***. Prandiano e EDF Tecnologia, São Paulo, 2013.
# 
# [7] SANTOS, E. D. F. da S. L.. ***Curso de python: radial basis function***. Prandiano e EDF Tecnologia, São Paulo, 2013.
# 
# [8] Universidade de São Paulo, Insituto de Ciências Matemáticas e de Computação. ***Redes neurais artificiais:*** Disponível em: <http://www.icmc.usp.br/pessoas/andre/research/neural/>.  Acessado em: 02/05/2014.
# 
# [9] Universidade Estadual de Maringá, Departamento de Informática. ***Neurais:*** Disponível em: <http://www.din.uem.br/ia/neurais/>. Acessado em: 09/05/2014.
# 
# [10] SANTOS, E. D. F. da S. L.; T., G. G.; MANCINI, W. D.. ***Comunicação da informação nas redes neurais artificiais***. Disciplina: BC0506 Comunicação e Redes. Prof. Dr. Itana Stiubiener. Santo André, SP, Brasil, 09 de maio de 2014.
# 
# [11] SANTOS, E. D. F. da S. L.. ***Projeto dirigido: funções de base radial.*** Universidade Federal do ABC (UFABC), Santo André, 2014.
# 
# [12] USER: OTHENEILDREW. ***Best readme template***. Disponível em: <https://github.com/othneildrew/Best-README-Template>. Acessado em: 21/02/2024 11:01
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 
