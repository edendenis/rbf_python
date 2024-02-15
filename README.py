#!/usr/bin/env python
# coding: utf-8

# # Pacote Propulsion Library `proplib`

# ## Resumo
# 
# Ferramentas computacionais para a equipe da APR, originado nas funções do repositório "GrandeMaquina".
# 
# ## _Abstract_
# 
# _Computational tools for the APR team, originating from the functions of the "GrandeMaquina" repository._

# ## Revisão(ões)/Versão(ões)
# 
# |Revisão número |Data da revisão |Descrição da revisão                                    |Autor da revisão         |
# |:-------------:|:--------------:|:-------------------------------------------------------|:------------------------|
# |0              |01/09/2022      |<ul><li>Revisão inicial/criação do documento.</li></ul> |<ul><li>Leonardo Lavra Rodrigues</li></ul> |
# |1              |19/01/2024      |<ul><li>Revisado todo o documento.</li></ul> <ul><li>Incluída Seções Padrão de desenvolvimento de Gráficos</li></ul> <ul><li>Incluída a Seção Cores das linhas</li></ul> <ul><li>Incluída a Seção Marcadores</li></ul> <ul><li>Incluída Seção Criar Chave SSH.</li></ul>|<ul><li>Eden Denis F. da S. L. Santos</li></ul>|
# |2              |23/01/2024      |<ul><li>Inserida a Seção Formatação de plotagem. </li></ul> <ul><li>Inserida a Seção Estilo de visualização de dados. </li></ul> <ul><li>Inserida a Seção Formatação de plotagem. </li></ul>|<ul><li>Augusto P. Rosa P. </li></ul> <ul><li>Eden Denis F. da S. L. Santos</li></ul>|
# |3              |27/01/2024      |<ul><li>Reestruturação do tutorial nas seções: </li></ul> <ul><li>1. Padronização, </li></ul> <ul><li>2. Guia de Instalação; e </li></ul> <ul><li>3. Exemplos de uso|<ul><li>Levi M. Araújo</li></ul>|
# |4              |30/01/2024      |<ul><li>Revisado pequenos textos.</li></ul>|<ul><li>Eden Denis F. da S. L. Santos</li></ul>|
# 

# ## 1. Padronização
# 
# ### 1.1 Padrão de idiomas de desenvolvimento dos códigos
# 
# Ao desenvolver um código, foi convencionado o padrão de idiomas abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de idiomas:
# 
# - **Classes, funções, parâmetros de funções, variáveis etc:** escrever em inglês;
# - **Comentários no código, commits, etc:** escrever em português brasileiro.

# ## 1.2 Padrão de desenvolvimentos do(s) gráfico(s)
# 
# #### 1.2.1 Cor(es) da(s) linha(s)
# 
# Ao desenvolver um código, foi convencionado o padrão de sequência de cores abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de cores:
# 
# 1. **Azul (Blue):** 'b'
# 2. **Laranja (Orange):** 'o'
# 3. **Verde (Green):** 'g'
# 4. **Vermelho (Red):** 'r'
# 5. **Roxo (Purple):** 'p'
# 6. **Marrom (Brown):** 'm'
# 7. **Rosa (Pink):** 'pink'
# 8. **Cinza (Gray):** 'gray'
# 9. **Amarelo (Yellow):** 'y'
# 10. **Ciano (Cyan):** 'c'
# 11. A partir de então a sequência de as cores fica à critério do desenvolver e, por ventura, pode ser alternada as cores para deixar o código intuítivo, por exemplo, usar o `orange` (laranja) para representar o Cobre e o `ray` (cinza) para representar o aço.
# 
# Essas são as cores padrão que você pode usar ao criar gráficos no Matplotlib em Python. Você pode especificar essas cores tanto por seus nomes quanto pelos códigos de uma letra correspondentes, como mostrado acima. Por exemplo, para criar um gráfico com pontos verdes, você pode usar 'g' como a cor.

# ### 1.2.2 Marcador(es)
# 
# Ao desenvolver um código, foi convencionado o padrão de sequência de marcador(es) abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de marcador(es)
# 
# 1. **Ponto (Dot):** '.'
# 2. **Círculo (Circle):** 'o'
# 3. **Triângulo para cima (Upward Triangle):** '^'
# 4. **Triângulo para baixo (Downward Triangle):** 'v'
# 5. **Triângulo para a esquerda (Left Triangle):** '<'
# 6. **Triângulo para a direita (Right Triangle):** '>'
# 7. **Quadrado (Square):** 's'
# 8. **Losango (Diamond):** 'D'
# 9. **Pentágono (Pentagon):** 'p'
# 10. **Hexágono (Hexagon):** 'h'
# 11. A partir de então a sequência de marcadores fica à critério do desenvolvedor.

# #### 1.2.3 Formatação de plotagem
# 
# Ao desenvolver um código, foi convencionado o padrão de formatação (tamanho da fonte do título, dos rótulos de eixos, da legenda, tamanho da figura, densidade de pixels etc.) abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de formatação:
# 
# 1. Importar o pacote `matplotlib.pyplot` para plotar os gráficos e, na sequência, inserir os comandos `rcParams` para ajustar e facilitar o estilo de visualização como segue:
# 
#     ```
#     import matplotlib.pyplot as plt
# 
#     plt.rcParams['figure.figsize'] = (16, 9)  # Tamanho da figura
#     plt.rcParams['font.family'] = 'serif'  # Escolha o tipo de fonte
#     plt.rcParams['font.size'] = 12  # Tamanho da fonte (NÂO especificada)
#     plt.rcParams["axes.labelsize"] = 14  # Tamanho da fonte do rótulo dos eixos
#     plt.rcParams["xtick.labelsize"] = 12  # Tamanho da fonte do eixo x
#     plt.rcParams["ytick.labelsize"] = 12  # Tamanho da fonte do eixo y
#     plt.rcParams["legend.fontsize"] = 12  # Tamanho da fonte da legenda
#     plt.rcParams['lines.linewidth'] = 2  # Espessura da(s) linha(s) plotadas
#     plt.rcParams['axes.grid'] = True  # Ativar a grade no gráfico
#     plt.rcParams['grid.alpha'] = 0.5  # Transparência da linha da grade
#     plt.rcParams["figure.dpi"] = 200  # Densidade mínima de pixels
# 
#     # Aproveite o melhor do ggplot e do seaborn
#     plt.style.use("ggplot")
#     plt.style.use("seaborn-deep")
# 
#     plt.rcParams["figure.autolayout"] = True
#     ```
# 
#     Pode ocorrer de serem gerados mais de um gráfico. Sendo assim, o padrão acima facilitará na formatação de todos os gráficos, logo, quando é alterado um dos parâmetros `rcParams`, essa alteração será executada em todos os gráficos, a menos que haja algum comando posterior ao padrão acima e que seja especifico para um determinado gráfico. 
#     
# **OBSERVAÇÃO(ÕES):**
# 
# - O tamanho da figura, caso tenha que ser alterado, deve seguir as proporções de 16:9;
# 
# - A fonte deve ser mantida o mais próximo da fonte do documento que o gráfico possa ser inserido (`doc`, `.docx`, `ods`, `.tex` etc.);
# 

# #### 1.2.4 Estilo de visualização de dados [4]
# 
# Ao desenvolver um código, foi convencionado o padrão de estilo abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de estilo:
# 
# 1. Importar o pacote `seaborn` para ajustar e facilitar o estilo de visualização de dados, portanto importar o pacote com o comando: `import seaborn as sns`
# 
# **OBSERVAÇÃO(ÕES):**
# 
# - A escola do estilo do `seaborn` (`darkgrid`, `whitegrid`, `dark`, `white`, `ticks` etc.) deve ser ajustada conforme for conveniente para a visualização do gráfico.

# #### 1.2.5 Quantidade de casas decimais no(s) gráfico(s)
# 
# Ao desenvolver um código, foi convencionado o padrão de quantidade de casas decimais nos gráficos abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de estilo:
# 
# 1. Para fins de visualização e arredondamento, por exemplo, de `[mm]` para `[m]` ou vice-versa, deve ser usado `4` casas decimais.
# 

# ### 1.3 Padrão de estilo e teste do código
# 
# #### 1.3.1 Instalação dos pacotes para a verificação de padrões
# 
# Para manter o código padronizado, inicialmente, instalar os pacote abaixo, como segue:
# 
# 1. Executar: `pip install pylint`;
# 
# 2. Executar: `pip install pytest`.
# 
# Ao desenvolver um código, foi convencionado o padrão de estilo abaixo. Logo, para manter o padrão, siga as instruções abaixo para o padrão de estilo:
# 
# - Ao instalar o pacote `pylint`, este, por sua vez, tem como dependência e já instala automaticamente os pacotes abaixo:
# 
#     - **Pacote Python Enhancement Proposals 8 (`pep8`)**: disponível em https://www.python.org/dev/peps/pep-0008/;
# 
#     - **Pacote Python Enhancement Proposals (`pep257`)**: disponível em(https://www.python.org/dev/peps/pep-0257/);
# 
# - Muitos editores e IDE's - `PyCharm`, `Spyder` e/ou `VS Code`, por exemplo - podem ser (ou já são) configurados para fazer verificação automática de adequação!;
# 
# - Recomendamos utilizar o `pylint` para verificação automática de estilo (`pip install pylint`);
# 
# - Executar o `pytest` na pasta raiz do `proplib`

# #### 1.3.2 Executar a verificação do padrão de estilo com o pacote `pylint`
# 
# Ao terminar o desenvolvimento de um código, execute os passos abaixo:
# 
# 1. No terminal, alterar o diretório para a pasta onde o código está armazenado: `cd /caminho/onde/o/codigo/esta/armazenado`;
# 
# 2. Execute o `pylint` no código com o comando: `pylint nome_do_codigo.py`;
# 
# 3. Teclar `Enter`;
# 
# 4. O resultado irá exibir o que está fora do padrão, os erros, os alertas e qual a nota o código recebeu. Sendo assim, foi convencionado que qualquer código, deve possuir uma nota maior ou igual a 6,50 (seis e meio) para que o código esteja em condições mínimas para ser composto ao pacote `proplib`:
#     * Caso o código tenha recebido uma nota inferior a 6,50 (seis e meio), corrigir os principais apontamentos.
# 
# 5. Caso tenha desenvolvido ou alterado mais códigos, executar o pacote `pylint` nos demais códigos.
# 
# #### 1.3.3 Executar a verificação do teste com o pacote `pytest`
# 
# Ao terminar o desenvolvimento de todos os códigos com o pacote `pylint` e realizar as correções dos principais apontamentos de maneira que os códigos tenham nota superior à `6,50` (seis e meio), executar os passos abaixo:
# 
# 1. No terminal, alterar o diretório para a pasta onde a pasta `proplib` está armazenado: `cd /caminho/onde/a/pasta/do/proplib/esta/armazenada/`;
# 
# 2. Executar o `pytest` na pasta: `pytest` (apenas digite `pytest`);
# 
# 3. Teclar `Enter`.
# 
# 4. O resultado irá exibir o que está fora do padrão, os erros, os alertas e qual a nota o código recebeu. Sendo assim, foi convencionado que qualquer código, deve possuir uma nota maior ou igual a 6,50 (seis e meio) para que o código esteja em condições mínimas para ser composto ao pacote `proplib`:
#     * Caso o código tenha recebido uma nota inferior a 6,50 (seis e meio), corrigir os principais apontamentos.

# ## 2. Guia de instalação

# ### 2.1 Instalar o Git
# 
# Verifique se você tem o Git instalado no seu computador. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/downloads
# 
# Abra o Git Bash. Você pode fazer isso clicando com o botão direito do mouse em qualquer diretório e selecionando a opção "Git Bash Here" no menu de contexto.

# ### 2.2 Criar chave SSH para a conta do usuário [1]
# 
# #### 2.2.1 Verificar se foi liberado o acesso ao Git
# 
# Antes de seguir os passos de uma das Seções abaixo (Linux e/ou Windows), confirmar com um dos administradores do Git se foi liberado o acesso para a sua conta de e-mail. Se não, solicitar o acesso antes de prosseguir com o passo a passo de uma Seções abaix (Linux e/ou Windows). 
# 
# #### 2.2.2 Linux
# 
# Para gerar uma chave SSH no Linux Ubuntu, você pode seguir os passos abaixo:
# 
# 1. Abra um terminal no seu sistema Ubuntu. Você pode fazer isso pressionando "Ctrl + Alt + T" ou procurando por "Terminal" no menu de aplicativos.
# 
# 2. No terminal, digite o seguinte comando para gerar um novo par de chaves SSH:
# 
#     `ssh-keygen -t rsa`
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

# #### 2.2.3 Windows [2]
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
# - Recomendamos instalar o pacote `proplib` no modo desenvolvedor/administrador!
# 
# - Clone o repositório:
#   
#   - pelo terminal: `$ git clone -b develop https://gitlab.com/iae-apr/proplib.git`
#   
#   - ou faça o download do repositório `.zip` pela página web do gitlab, botão ao lado do botão azul "clone" à direita
# 
# - Abra um terminal na raiz do repositório (pasta `proplib`, com subpastas "docs", "tests", etc);
# 
# - execute o comando a seguir no terminal:  `$ sudo pip install -e .` (o ponto faz parte do comando!)
#   
#   - Caso o comando acima **NÃO** funcione, isto pode significar que você **NÃO** tem previlégios para instalar o pacote na pasta raíz (root) do Sistema Operacional (SO). Sendo assim, execute o comando a seguir no terminal: `pip install -e .` (**SEM** o `sudo`), desta maneira você conseguirá instalar o `setup.py` no diretório de usuário.

# #### Windows
# 
# - Recomendamos instalar o pacote `proplib` no modo desenvolvedor/administrador!
# 
# - Clone o repositório:
#   
#   - pelo terminal: `$ git clone https://gitlab.com/iae-apr/proplib.git`
#   
#   - ou faça o download do repositório `.zip` pela página web do gitlab, botão ao lado do botão azul "clone" à direita
# 
# - Abra um terminal na raiz do repositório (pasta `proplib`, com subpastas "docs", "tests", etc);
# 
# - execute o comando a seguir no terminal:  `$ sudo pip install -e .` (o ponto faz parte do comando!)
#   
#   - Caso o comando acima **NÃO** funcione, isto pode significar que você **NÃO** tem previlégios para instalar o pacote na pasta raíz (root) do Sistema Operacional (SO). Sendo assim, execute o comando a seguir no terminal: `pip install -e .` (**SEM** o `sudo`), desta maneira você conseguirá instalar o `setup.py` no diretório de usuário.

# ### 2.5 Como testar
# 
# - Rodar o comando `pytest` ou `pytest3` (caso não o tenha instalado, `pip install pytest`), na raiz do repositório ou junto a cada módulo. 

# ## 3. Exemplos de uso
# 
# ### 3.1 Usando interativamente em um terminal python/ipython:
# 
# De dentro de um terminal python/ipython, basta importar o `proplib` (como se fosse o `numpy`) com o comando:
# `>>> import proplib`
# 
# Alternativamente, todas as funções principais do `proplib` podem ser importadas individualmente. Digamos que se quer saber a densidade do oxigênio líquido a $ 100 K $ e $ 100 bar $:
# 
# ```
# >>> from proplib import get_dens
# >>> get_dens('oxygen', pres=100e5, temp=100)
# 1116.286535964689
# ```

# ## 3.2 Como rodar um caso de análise de câmara utilizando o `TCA_main`:
# 
# - Ao instalar o `proplib`, o comando `TCA_main` fica disponível no terminal em qualquer diretório;
# 
# - A sintaxe básica é `$ TCA_main caminho/ate/o/seu/arquivo/input/desejado.py` (a extensão é opcional);
# 
# - Este comando executa a análise da câmara cujos parâmetros estão no arquivo de input que você selecionou;
#   
#   - Logo, é mais fácil abrir um terminal na pasta onde está o seu arquivo (digamos, `exemplo.py`) e rodar `$ TCA_main exemplo.py`, por exemplo.
# 
# - Alternativamente, alguns casos "clássicos" estão disponíveis com palavras-chaves:
#   
#   - exemplo: `TCA_main rd107`
# 
# ### 3.2.1 O que exatamente é executado ao rodar `TCA_main`?
# 
# - Este atalho executa a função `main()` do módulo `proplib/main_files/LPRE_main_files/TCA_main.py`;
# 
# - Daí, será instanciado um objeto representando o Conjunto da Câmara de Empuxo (classe `ThrustChamberAssembly` (TCA), armazenada em `proplib/proplib/LPRE_lib/components/thrust_chamber_assembly/TCA.py`);
# 
# - E em seguida, será executada uma função (tecnicamente, um método) deste objeto, conforme o conteúdo do campo `self.procedure` no seu `input`;
# 
# - Se `self.procedure` for `TCA_analysis` (o mais comum), vai ser rodado o método `analysis()`, que consiste em:
#   
#   - **`performance.basic_calculations`:** calculo básico dos principais parâmetros da câmara de empuxo (vazão, estimativa de $ I_{sp} $ etc);
#   
#   - **`geometry.generate_internal_contour`:** projeto/dimensionamento do contorno da câmara;
#   
#   - **`stability.acoustic_modes`:** cálculo dos modos acústicos;
#   
#   - **`cooling.thermal_analysis`:** análise térmica da câmara;
#   
#   - **`structure.cooling_jacket_structural_analysis`:** análise estrutural da jaqueta;
#   
#   - **`structure.radiative_nozzle_preliminary_structural_analysis`:** análise estrutural preliminar da tubeira radiativa (se houver);
#   
#   - **`output.print_thermal_results_to_csv`:** geração do arquivo de resultados da análise térmica.
# 
# - Resultados desta rodada:
#   
#   - Muitas linhas de texto "printadas" no seu terminal (embora tentemos filtrar apenas o essencial...);
#   
#   - Alguns gráficos (ou não, dependendo do conteúdo do seu input)
#   
#   - Uma pasta com a data e a hora atuais (e.g. `2022_07_20_10_56_44_452309`), contendo: 
#     
#     - Uma cópia do seu arquivo de input (`.py`);
#     
#     - Um arquivo de registro (`.log`); e 
#     
#     - Um arquivo dos resultados da análise térmica (.csv)

# ### 3.3 Outros "macrocomandos" com atalhos no terminal:
# 
# - **`pump_main`:** mesma filosofia `TCA_main`, mas para bombas!
# 
# - **`sign_sha1`:** renomeia o arquivo de input desejado, inserindo sua assinatura SHA1
#   
#   - ex: `$ sign_sha1 arquivo.py` transforma o `arquivo.py` em `arquivo_9a38fe4b.py`
# 
# - **`compare_inputs`:** compara dois arquivos de input, vendo as diferenças entre eles
#   
#   - ex: `$ compare_inputs input1.py este/esta/em/outra/pasta/input2.py`

# ## 4. Links para outros tutoriais úteis relacionados ao pacote `proplib`
# 
# - Tutorial sobre base de dados no `prolib`: https://gitlab.com/iae-apr/proplib/-/tree/develop/proplib/util/properties/material_properties_database#tutorial-base-de-dados 

# ## Referências
# 
# [1] OPENAI. ***Gerar chave ssh ubuntu:*** https://chat.openai.com/c/6f3224a3-b4a2-43c6-a878-f1612beae966 (texto adaptado). Chat GPT. Acessado em: 21/07/2023 10:14.
# 
# [2] OPENAI. ***Gerar chave ssh ubuntu:*** https://chat.openai.com/c/3d4690a0-2466-4655-990a-cd14823b6825 (texto adaptado). Chat GPT. Acessado em: 21/07/2023 10:21.
# 
# [3] OPENAI. ***Instalação local usando o `pip`:** https://chat.openai.com/?model=text-davinci-002-render-sha (texto adaptado). Chat GPT. Acessado em: 25/07/2023 13:51.
# 
# [4] SEABORN. ***Seaborn: statistical data visualization:*** https://seaborn.pydata.org/. Seaborn team. Acessado em: 23/01/2024 11:05.
