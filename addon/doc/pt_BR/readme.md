# StationPlaylist #

* Autores: Christopher Duffley <nvda@chrisduffley.com> (anteriormente Joseph
  Lee <joseph.lee22590@gmail.com>, originalmente por Geoff Shang e outros
  colaboradores)

Este pacote de complemento fornece uso aprimorado do StationPlaylist Studio
e outros aplicativos StationPlaylist, além de fornecer utilitários para
controlar o Studio de qualquer lugar. Os aplicativos compatíveis incluem
Studio, Criador — Criador —, Track Tool — Ferramenta de Faixa —, VT Recorder
e Streamer, bem como codificadores — encoders — SAM, SPL e AltaCast.

Para obter mais informações sobre o add-on, leia o [guia do add-on][1].

NOTAS IMPORTANTES:

* Esse complemento requer o StationPlaylist Suite 5.50 ou posterior.
* Alguns recursos complementares serão desativados ou limitados se o NVDA
  estiver sendo executado em modo seguro, como na tela de logon.
* Para obter a melhor experiência, desative o modo de redução de áudio.
* A partir de 2018, [changelogs para versões antigas do complemento][2]
  serão encontrados no GitHub. Este Leiame do complemento listará as
  alterações da versão 25.01 (2025) em diante.
* Enquanto o Studio está em execução, você pode salvar, recarregar as
  configurações salvas ou redefinir as configurações do complemento para os
  padrões pressionando Control+NVDA+C, Control+NVDA+R uma vez ou
  Control+NVDA+R três vezes, respectivamente. Isso também se aplica às
  configurações do codificador - você pode salvar e redefinir (não
  recarregar) as configurações do codificador se estiver usando
  codificadores.
* Muitos comandos fornecerão saída de fala enquanto o NVDA estiver no modo
  falar sob demanda (NVDA 2024.1 e posterior).

## Teclas de atalho

A maioria deles funcionará somente no Studio, a menos que especificado de
outra forma. Salvo indicação em contrário, esses comandos suportam o modo de
fala sob demanda.

* Alt+Shift+T na janela do Studio: anuncia o tempo decorrido para a faixa
  atualmente em reprodução.Alt+Shift+T na janela do Studio: anuncia o tempo
  decorrido para a faixa atualmente em reprodução.
* Control+Alt+T (toque com dois dedos para baixo no modo SPL touch) na
  janela Studio: anuncia o tempo restante da faixa atualmente em reprodução.
* NVDA+Shift+F12 (deslizar com dois dedos para cima no modo tátil SPL) na
  janela do Studio: anuncia o tempo da emissora como 5 minutos para o início
  da hora. Pressionar este comando duas vezes anunciará os minutos e
  segundos até o início da hora.
* Alt+NVDA+1 (movimento de dois dedos para a direita no modo SPL) na janela
  do Studio: Abre a categoria de alarmes na caixa de diálogo de configuração
  do complemento do Studio (não suporta falar sob demanda).
* Alt+NVDA+1 no Editor de Lista de Reprodução do Creador e no editor de
  lista de reprodução Remote VT: Anuncia a hora programada para a lista de
  reprodução — playlist — carregada.
* Alt+NVDA+2 no Editor de Lista de Reprodução do Criador e editor de lista
  de reprodução Remote VT: Anuncia a duração total da lista de reprodução.
* Alt+NVDA+3 na janela do Studio: Alterna o explorador de carrinhos para
  aprender as atribuições de carrinhos (não suporta falar sob demanda).
* Alt+NVDA+3 no Editor de Lista de Reprodução do Criador e editor de lista
  de reprodução Remote VT: Anuncia quando a faixa selecionada está
  programada para tocar.
* Alt+NVDA+4 no Editor de Lista de Reprodução do Criador e editor de lista
  de reprodução Remote VT: Anuncia rotação e categoria associada à lista de
  reprodução carregada.
* Control+NVDA+F na janela do Studio: Abre uma caixa de diálogo para
  localizar uma faixa com base no nome do artista ou da música. Pressione
  NVDA+F3 para procurar para frente ou NVDA+Shift+F3 para procurar para trás
  (não suporta falar sob demanda).
* Shift+NVDA+R na janela do Studio: Percorre as configurações de anúncio de
  varredura da biblioteca (não suporta falar sob demanda).
* Control+Shift+X na janela do Studio: Percorre as configurações do
  temporizador em braile (não suporta falar sob demanda).
* Control+Alt+seta para a esquerda/direita (enquanto estiver focado em uma
  faixa no Studio, Criador, Remote VT e Ferramenta de rastreamento): Mover
  para a coluna da faixa anterior/seguinte (não suporta falar sob demanda).
* Control+Alt+seta para cima/para baixo (enquanto estiver focado em uma
  faixa no Studio, Criador, Remote VT e Track Tool): Move para a faixa
  anterior/próxima e anuncia colunas específicas (não suporta falar sob
  demanda).
* Control+NVDA+1 a 0 (enquanto focalizado numa faixa no Studio, Criador
  (incluindo o Editor de Lista de Reprodução), Remote VT e ferramenta de
  Faixa): Anuncia o conteúdo da coluna para uma coluna especificada (as
  primeiras dez colunas por padrão). Pressionar este comando duas vezes
  exibirá as informações da coluna numa janela em modo de navegação.
* Control+NVDA+- (hífen enquanto estiver focado em uma faixa no Studio,
  Criador, Remote VT e Track Tool): exibe dados de todas as colunas em uma
  faixa em uma janela de modo de navegação (não suporta falar sob demanda).
* NVDA+V enquanto estiver focado em uma faixa (somente no visualizador de
  listas de reprodução do Studio): alterna o anúncio da coluna da faixa
  entre a ordem da tela e a ordem personalizada (não suporta falar sob
  demanda).
* Alt+NVDA+C enquanto focalizado numa faixa (somente visualizador da lista
  de reprodução do Studio): anuncia os comentários da faixa, se houver.
* Alt+NVDA+0 na janela do Studio: Abre a caixa de diálogo de configuração do
  add-on do Studio (não suporta falar sob demanda).
* Alt+NVDA+P na janela do Studio: Abre a caixa de diálogo de perfis de
  transmissão do Studio (não suporta falar sob demanda).
* Alt+NVDA+F1: Abre a caixa de diálogo de boas-vindas (não oferece suporte
  para falar sob demanda).

## Comandos não atribuídos

Os comandos a seguir não são atribuídos por padrão; se desejar atribuí-los,
use o diálogo Definir comandos — Gestos de entrada — para adicionar comandos
personalizados. Para fazer isso, na janela do Studio, abra o menu NVDA,
Preferências e Definir comandos. Expanda a categoria StationPlaylist,
localize os comandos não atribuídos na lista abaixo e selecione "Adicionar"
e digite o comando — gesto — que deseja usar.

Importante: alguns desses comandos não funcionarão se o NVDA estiver sendo
executado em modo seguro, como na tela de login. Nem todos os comandos são
compatíveis com a fala sob demanda.

* Alternar para a janela do SPL Studio a partir de qualquer programa
  (indisponível no modo seguro, não suporta falar sob demanda).
* Camada do controlador SPL (indisponível no modo seguro).
* Anúncio do status do Studio, como a reprodução de faixas de outros
  programas (indisponível no modo seguro).
* Anúncio do status da conexão do codificador a partir de qualquer programa
  (indisponível no modo seguro).
* Camada Assistente SPL do SPL Studio.
* Anuncia o tempo incluindo segundos, do SPL Studio.
* Anúncio da temperatura.
* Anúncio do título da próxima faixa, se programada.
* Anúncio do título da faixa atualmente em reprodução.
* Marcando a faixa atual para o início da análise do tempo da faixa.
* Executando análise de tempo da faixa.
* Tira instantâneos — da lista de reprodução.
* Localiza texto em colunas específicas (não suporta falar sob demanda).
* Localize faixas com duração que se enquadre em um determinado intervalo
  por meio do localizador de intervalo de tempo (não suporta falar sob
  demanda).
* Ative ou desative rapidamente o streaming de metadados (não é compatível
  com o recurso falar sob demanda).

## Comandos adicionais ao usar codificadores

Os comandos a seguir estão disponíveis ao usar codificadores e os usados
para alternar opções de comportamento na conexão, como focar no Studio,
reproduzir a primeira faixa e alternar o monitoramento em segundo plano,
podem ser atribuídos por meio da caixa de diálogo Gestos de entrada no menu
NVDA, Preferências, Gestos de entrada, na categoria StationPlaylist. Esses
comandos não são compatíveis com a fala sob demanda.

* F9: conecte o codificador selecionado.
* F10 (somente codificador SAM): Desconecte o codificador selecionado.
* Control+F9: Conecte todos os codificadores.
* Control+F10 (somente codificador SAM): Desconecte todos os codificadores.
* Control+Shift+F11: alterna se o NVDA mudará para a janela do Studio para o
  codificador selecionado, se estiver conectado.
* Shift+F11: Define se o Studio reproduzirá a primeira faixa selecionada
  quando o codificador estiver conectado a um servidor de fluxo — streaming.
* Control+F11: Alterna o monitoramento em segundo plano do codificador
  selecionado.
* Control+F12: abre um diálogo para selecionar o codificador que você
  excluiu (para realinhar os rótulos e as configurações do codificador).
* Alt+NVDA+0 ou F12: Abre a caixa de diálogo de configurações do codificador
  para configurar opções como a etiqueta do codificador.

Além disso, os comandos de revisão de coluna estão disponíveis, incluindo
(suporta falar sob demanda):

* Control+NVDA+1: Posição do codificador.
* Control+NVDA+2: rótulo do codificador.
* Control+NVDA+3 no codificador SAM: formato do codificador.
* Control+NVDA+3 no SPL e no Codificador AltaCast: Configurações do
  codificador.
* Control+NVDA+4 no codificador SAM: Status de conexão do codificador.
* Control+NVDA+4 no SPL e no Codificador AltaCast: Taxa de transferência ou
  status da conexão.
* Control+NVDA+5 no codificador SAM: descrição do status da conexão.

## Camada Assistente SPL

Este conjunto de comandos de camada permite obter vários status no SPL
Studio, como se uma faixa está sendo reproduzida, duração total de todas as
faixas durante a hora e assim por diante. Em qualquer janela do SPL Studio,
pressione o comando da camada Assistente SPL e, em seguida, pressione uma
das teclas da lista abaixo (um ou mais comandos são exclusivos do
visualizador da lista de reprodução). Você também pode configurar o NVDA
para emular comandos de outros leitores de tela.

Os comandos disponíveis são (a maioria dos comandos é compatível com a fala
sob demanda):

* A: Automatização.
* C (Shift+C no leiaute JAWS): Título para a faixa atualmente em reprodução.
* C (layout do JAWS): Alternar o explorador de carrinhos (somente
  visualizador de lista de reprodução, não oferece suporte a fala sob
  demanda).
* D (R no leiaute JAWS): Duração restante para a lista de reprodução (se uma
  mensagem de erro for dada, mova para o visualizador da lista de reprodução
  e, em seguida, execute este comando).
* Control+D (Studio 6.10 e posterior): Teclas de controle
  habilitadas/desabilitadas.
* E: Status de fluxo de metadados.
* Shift+1 a Shift+4, Shift+0: status para URLs de fluxo — streaming — de
  metadados individuais (0 é para codificador DSP).
* F: Localizar faixa (somente visualizador de lista de reprodução, não é
  compatível com fala sob demanda).
* H: Duração da música para a hora de programação.
* Shift+H: duração restante da faixa para a hora de programação.
* I (L no leiaute JAWS): Contagem de ouvintes.
* K: Mova para a faixa marcada (somente visualizador da lista de
  reprodução).
* Control+K: Defina a faixa atual como a faixa do marcador de lugar (somente
  visualizador de lista de reprodução).
* L (Shift+L no leiaute JAWS): Entrada de linha.
* M: Microfone.
* N: Título para a próxima faixa programada.
* O: Fim da hora da lista de reprodução/sob por.
* P: Status de reprodução (reproduzindo ou parado).
* Shift+P: Tonalidade — pitch — da faixa atual.
* * R (Shift+E no leiaute JAWS): Gravar no arquivo habilitado/desabilitado.
* Shift+R: Monitora a varredura da biblioteca em andamento.
* S: A faixa começa (programada).
* Shift+S: tempo até que a faixa selecionada seja reproduzida (a faixa
  começa em).
* T: Modo de edição/inserção do carrinho ativado/desativado.
* U: Tempo em atividade do Studio.
* W: Clima e temperatura, se configurados.
* Y: Status modificado da lista de reprodução.
* F8: Tire instantâneos da lista de reprodução (número de faixas, faixa mais
  longa, etc.).
* Shift+F8: Solicita transcrições da lista de reprodução em vários formatos.
* F9: Marca a faixa atual para o início da análise da lista de reprodução
  (somente visualizador da lista de reprodução).
* F10: Executa a análise de tempo da faixa (somente visualizador da lista de
  reprodução).
* F12: Alternar entre o perfil atual e um predefinido.
* F1: Ajuda da camada.

## Controlador SPL

O Controlador SPL é um conjunto de comandos em camadas que você pode usar
para controlar o SPL Studio de qualquer lugar. Pressione o comando da camada
Controlador SPL e o NVDA dirá, "Controlador SPL". Pressione outro comando
para controlar várias configurações do Studio, como ligar/desligar o
microfone ou reproduzir a próxima faixa.

Importante: os comandos da camada do controlador SPL são desativados se o
NVDA estiver sendo executado em modo seguro.

Os comandos do controlador SPL disponíveis são (alguns comandos suportam
falar sob demanda):

* P: reproduz a próxima faixa selecionada.
* U: pausa ou retoma a reprodução.
* S: Para a faixa com enfraquecimento — fade out.
* T: Parada instantânea.
* M: Liga o microfone.
* Shift+M: Desliga o microfone.
* N: Liga o microfone sem desvanecimento.
* A: Ativa a automatização.
* Shift+A: Desativa a automatização.
* L: Ativa entrada de linha.
* Shift+L: Desativa a entrada de linha.
* R: Tempo restante para a faixa atualmente em reprodução.
* Shift+R: Progresso da varredura da biblioteca.
* C: Título e duração da faixa que está sendo reproduzida no momento
  (suporta falar sob demanda).
* Shift+C: Título e duração da próxima faixa, se houver (suporta falar sob
  demanda).
* E: Status da conexão do codificador (suporta fala sob demanda).
* I: Contagem de ouvintes (suporta falar sob demanda).
* P: Informações sobre o status do estúdio, como se uma faixa está sendo
  reproduzida, se o microfone está ligado e outras (suporta falar sob
  demanda).
* Teclas do carrinho (F1, Control+1, por exemplo): Reproduz carrinhos
  atribuídos de qualquer lugar.
* H: Ajuda da camada.

## Alarmes de faixa e microfone

Por padrão, o NVDA irá tocar um bipe se faltarem cinco segundos na faixa
(outro) e/ou introdução, bem como ouvir um bipe se o microfone estiver ativo
por um tempo. Para configurar alarmes de faixa e microfone, pressione
Alt+NVDA+1 para abrir as configurações de alarmes na tela de configurações
do complemento do Studio. Também pode usar essa tela para configurar se
ouvirá um bipe, uma mensagem ou ambos quando os alarmes forem ativados.

## Localizador de Faixa

Se você deseja localizar rapidamente uma música por um intérprete ou pelo
nome da música, na lista de faixas, pressione Control+NVDA+F. Digite ou
escolha o nome do intérprete ou o nome da música. O NVDA irá colocá-lo na
música se for localizada ou exibirá um erro se não puder encontrar a música
que você está procurando. Para localizar uma música ou intérprete digitado
anteriormente, pressione NVDA+F3 ou NVDA+Shift+F3 para localizar pra frente
ou pra trás.

Nota: Localizador de Faixa diferencia maiúsculas de minúsculas.

## Explorador de carrinho

Dependendo da edição, o SPL Studio permite que até 96 carrinhos sejam
atribuídos para reprodução. O NVDA permite que você ouça qual carrinho ou
jingle está atribuído a esses comandos.

Para aprender as atribuições do carrinho, no SPL Studio, pressione
Alt+NVDA+3. Pressionar o comando do carrinho uma vez informará qual jingle
está atribuído ao comando. Pressione o comando do carrinho duas vezes para
reproduzir o jingle. Pressione Alt+NVDA+3 para sair do explorador do
carrinho. Consulte o guia do complemento para obter mais informações sobre o
explorador de carrinho.

## Análise de tempo de faixa

Para obter a duração da reprodução das faixas selecionadas, marque a faixa
atual para o início da análise do tempo da faixa (Assistente SPL, F9) e
pressione Assistente SPL, F10 quando chegar ao final da seleção.

## Explorador de colunas

Pressionando Control+NVDA+1 a 0, você pode obter o conteúdo de colunas
específicas. Por padrão, essas são as primeiras dez colunas para um item de
faixa (no Studio: intérprete, título, duração, introdução, outro, categoria,
ano, álbum, gênero, modo). Para o editor de lista de reprodução no Criador e
cliente Remote VT, os dados da coluna dependem da ordem das colunas,
conforme mostrada na tela. No Studio, lista de faixas principal do Criador,
e Ferramenta de Faixa, os espaços de coluna são predefinidos
independentemente da ordem das colunas na tela e podem ser configurados no
diálogo de configurações do complemento na categoria de explorador de
colunas.

## Anúncio da coluna de faixa

Você pode pedir ao NVDA para anunciar as colunas das faixas encontradas no
visualizador da lista de reprodução do Studio na ordem em que aparecem na
tela ou usando uma ordem personalizada e/ou excluir certas
colunas. Pressione NVDA+V para alternar este comportamento enquanto focaliza
uma faixa no visualizador de lista de reprodução do Studio. Para
personalizar a inclusão e a ordem das colunas, no painel de configurações de
anúncio da coluna nas configurações do complemento, desmarque "Anunciar
colunas na ordem mostrada na tela" e, em seguida, personalize as colunas
incluídas e/ou a ordem das colunas.

## Instantâneos da lista de reprodução

Você pode pressionar Assistente SPL, F8 enquanto estiver focalizado numa
lista de reprodução no Studio para obter várias estatísticas sobre uma
playlist, incluindo o número de faixas na lista de reprodução, a faixa mais
longa, os principais intérpretes e assim por diante. Depois de atribuir um
comando personalizado para este recurso, pressionar o comando personalizado
duas vezes fará com que o NVDA apresente informações instantâneas da lista
de reprodução como uma página web para que você possa usar o modo de
navegação para navegar (pressione Esc para fechar).

## Transcrições da Lista de Reprodução

Pressionando Assistente SPL, Shift+F8 apresentará um diálogo para permitir
que você solicite transcrições da lista de reprodução em vários formatos,
incluindo um formato de texto simples, uma tabela HTML ou uma lista.

## Diálogo de configuração

Na janela do estúdio, você pode pressionar Alt+NVDA+0 para abrir a caixa de
diálogo de configuração do complemento. Como alternativa, acesse o menu de
preferências do NVDA e selecione o item Configurações do SPL Studio. Nem
todas as configurações estarão disponíveis se o NVDA estiver sendo executado
em modo seguro.

## Diálogo de perfis de transmissão

Você pode salvar as configurações de programas específicos em perfis de
transmissão — broadcast. Esses perfis podem ser gerenciados por meio do
diálogo de perfis de transmissão SPL, que pode ser acessado pressionando
Alt+NVDA+P na janela do Studio.

## Modo tátil SPL

Se você estiver usando o Studio em um computador com tela sensível ao toque
e com o NVDA instalado, pode executar alguns comandos do Studio a partir da
tela sensível ao toque. Primeiro, use o toque de três dedos para alternar
para o modo SPL e, em seguida, use os comandos de toque listados acima para
executar os comandos.

## Version 25.06.3-LTS

* In Studio's playlist viewer, NVDA will no longer appear to do nothing or
  play error tones when reporting column contents if vertical column
  navigation is set to values other than "whichever column I am reviewing".
* Setting vertical column navigation to "Status" column is deprecated and
  will be removed in a future add-on release.

## Version 25.06.2-LTS

* Columns explorer (Control+NVDA+number row) is now configurable for Creator
  and Remote VT's playlist editor. A new button, "columns explorer for
  playlist editor" is available from columns explorer add-on settings
  screen.
* In columns explorer add-on settings, renamed "columns explorer" to
  "columns explorer for SPL Studio".
* Added JSON (JavaScript Object Notation) format as a playlist transcripts
  format.
* In encoders, NVDA will remove encoder settings if pressing Control+F12 to
  remove settings for encoder 10 and above if more than ten encoders are
  present.

## Versão 25.06-LTS

A versão 25.06.x é a última série de versões compatíveis com o Studio 5.x,
sendo que as versões futuras exigirão o Studio 6.x. Alguns novos recursos
serão transferidos para a versão 25.06.x, se necessário.A versão 20.09.x é a
última série de lançamento a suportar o Studio 5.20 e baseada em tecnologias
antigas, com versões futuras suportando o Studio 5.30 e recursos mais
recentes do NVDA. Alguns novos recursos serão portados para 20.09.x, se
necessário.

* Internal changes to make the add-on more compatible with upcoming 64-bit
  NVDA.
* O NVDA não se esquecerá mais de transferir perfis de transmissão ao
  atualizar o complemento (corrigindo uma regressão introduzida na versão
  25.05).
* Adição de um novo comando no SPL Assistant para anunciar a hora da lista
  de reprodução acima/abaixo em minutos e segundos (O).
* No Studio, o comando para percorrer as configurações de anúncio de
  varredura da biblioteca foi alterado de Alt+NVDA+R para Shift+NVDA+R, pois
  o primeiro comando ativa o recurso de acesso remoto no NVDA 2025.1.
* O NVDA não reproduzirá mais tons de erro ou parecerá não fazer nada ao
  executar alguns comandos do SPL Assistant depois de redimensionar a janela
  do Studio.
* A interface do usuário para a caixa de diálogo de confirmação exibida ao
  excluir perfis de transmissão agora se assemelha à interface de exclusão
  de perfil de configuração do NVDA.
* Nas configurações do complemento, o NVDA não moverá mais o foco do teclado
  para o botão OK após fechar o explorador de colunas e as caixas de diálogo
  de redefinição.
* O NVDA reconhecerá as alterações de coluna de trilha introduzidas no
  Criador e no Track Tool 6.11.
* No explorador de colunas do Criador, a coluna “Restrição de data” agora é
  “Restrições”.
* O NVDA não reproduzirá mais carrinhos errados ao reproduzi-los por meio da
  camada do controlador SPL.

## Versão 25.05

* É necessário o NVDA 2024.1 ou posterior devido à atualização do Python
  3.11.
* Suporte limitado restaurado para o Windows 8.1.
* Movemos os documentos wiki de complementos, como o changelog de
  complementos, para o repositório de código principal.
* Foi adicionado  o botão Fechar às telas de instantâneos de listas de
  reprodução, transcrições de listas de reprodução e ajuda do SPL Assistant
  e da camada Controller (NVDA 2025.1 e posterior).
* O NVDA não fará mais nada ou reproduzirá tons de erro ao anunciar
  informações sobre clima e temperatura no Studio 6.1x (SPL Assistant, W).

## Versão 25.01

* É necessário o Windows 10 21H2 (build 19044) de 64 bits ou posterior.
* Os links de download para versões de complemento não estão mais incluídos
  na documentação do complemento. Você pode fazer o download do complemento
  na loja de complementos da NV Access.
* Mudança da ferramenta de linting do Flake8 para o Ruff e reformatação dos
  módulos complementares para melhor alinhamento com os padrões de
  codificação do NVDA.
* No Studio 6.10 e posterior, foi adicionado um novo comando no SPL
  Assistant para anunciar o status de ativação/desativação das teclas de
  controle (Control+D).
* No Studio 6.10 e posterior, foi adicionado um novo comando no SPL
  Assistant para anunciar o status de ativação/desativação das teclas de
  controle (Control+D).

## Versões mais antigas

Consulte o [changelog][2] para obter as notas de versão das versões antigas
do complemento.

[1]:
https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
