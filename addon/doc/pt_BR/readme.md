# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee e outros contribuidores
* Baixe a [versão estável][1]
* Compatibilidade com NVDA: 2020.4 e além

Este pacote de complemento fornece uso aprimorado do StationPlaylist Studio
e outros aplicativos StationPlaylist, além de fornecer utilitários para
controlar o Studio de qualquer lugar. Os aplicativos compatíveis incluem
Studio, Creator — Criador —, Track Tool — Ferramenta de Faixa —, VT Recorder
e Streamer, bem como codificadores — encoders — SAM, SPL e AltaCast.

Para obter mais informações sobre o complemento, leia o [guia do
complemento][2].

NOTAS IMPORTANTES:

* Este complemento requer a suíte StationPlaylist 5.30 ou posterior.
* Se estiver usando o Windows 8 ou posterior, para obter a melhor
  experiência, desative o modo de áudio prioritário (redução de áudio).
* A partir de 2018, os changelogs — registro de alterações — para versões
  antigas de complementos serão encontrados no GitHub. Este readme — leia-me
  — do complemento irá listar as alterações da versão 20.09 (2020) em
  diante.
* Enquanto o Studio está em execução, você pode salvar, recarregar as
  configurações salvas ou redefinir as configurações do complemento para os
  padrões pressionando Control+NVDA+C, Control+NVDA+R uma vez ou
  Control+NVDA+R três vezes, respectivamente. Isso também se aplica às
  configurações do codificador - você pode salvar e redefinir (não
  recarregar) as configurações do codificador se estiver usando
  codificadores.

## Teclas de atalho

A maioria delas funcionará no Studio apenas a menos que seja especificado de
outra forma.

* Alt+Shift+T na janela do Studio: anuncia o tempo decorrido para a faixa
  atualmente em reprodução.
* Control+Alt+T (deslizar dois dedos para baixo no modo tátil SPL) na janela
  do Studio: anuncia o tempo restante para a faixa atualmente em reprodução.
* NVDA+Shift+F12 (deslizar com dois dedos para cima no modo tátil SPL) na
  janela do Studio: anuncia o tempo da emissora como 5 minutos para o início
  da hora. Pressionar este comando duas vezes anunciará os minutos e
  segundos até o início da hora.
* Alt+NVDA+1 (deslizar com dois dedos para a direita no modo tátil SPL) na
  janela do Studio: Abre a categoria de alarmes na caixa de diálogo de
  configuração do complemento do Studio.
* Alt+NVDA+1 no Editor de Lista de Reprodução do Creator e no editor de
  lista de reprodução Remote VT: Anuncia a hora programada para a lista de
  reprodução — playlist — carregada.
* Alt+NVDA+2 no Editor de Lista de Reprodução do Creator e editor de lista
  de reprodução Remote VT: Anuncia a duração total da lista de reprodução.
* Alt+NVDA+3 na janela do Studio: Alterna o explorador do carrinho — cart —
  para aprender as atribuições de carrinho.
* Alt+NVDA+3 no Editor de Lista de Reprodução do Creator e editor de lista
  de reprodução Remote VT: Anuncia quando a faixa selecionada está
  programada para tocar.
* Alt+NVDA+4 no Editor de Lista de Reprodução do Creator e editor de lista
  de reprodução Remote VT: Anuncia rotação e categoria associada à lista de
  reprodução carregada.
* Control+NVDA+f na janela do Studio: Abre um diálogo para localizar uma
  faixa baseada no intérprete ou nome da música. Pressione NVDA+F3 para
  localizar para frente ou NVDA+Shift+F3 para localizar para trás.
* Alt+NVDA+R na janela do Studio: Passa pelas configurações de anúncio de
  varredura — scan — da biblioteca.
* Control+Shift+X na janela do Studio: Passa pelas configurações do
  temporizador braille.
* Control+Alt+seta para esquerda/direita (enquanto focalizado numa faixa no
  Studio, Creator, Remote VT e Ferramenta de Faixa): Move-se para a coluna
  anterior/seguinte da faixa.
* Control+Alt+Home/End (enquanto focalizado numa faixa no Studio, Creator,
  Remote VT e Ferramenta de Faixa): Move-se para a primeira/última coluna da
  faixa.
* Control+Alt+seta para cima/baixo (enquanto focalizado numa faixa no
  Studio, Creator, Remote VT e ferramenta de Faixa): Move-se para a faixa
  anterior/seguinte e anuncia colunas específicas.
* Control+NVDA+1 a 0 (enquanto focalizado numa faixa no Studio, Creator
  (incluindo o Editor de Lista de Reprodução), Remote VT e ferramenta de
  Faixa): Anuncia o conteúdo da coluna para uma coluna especificada (as
  primeiras dez colunas por padrão). Pressionar este comando duas vezes
  exibirá as informações da coluna numa janela em modo de navegação.
* Control+NVDA+- (hífen enquanto focalizado numa faixa no Studio, Creator,
  Remote VT e Ferramenta de Faixa): exibe dados para todas as colunas numa
  trilha em uma janela do modo de navegação.
* NVDA+V enquanto focalizado numa faixa (somente visualizador de lista de
  reprodução do Studio): alterna o anúncio da coluna da faixa entre a ordem
  da tela e a ordem personalizada.
* Alt+NVDA+C enquanto focalizado numa faixa (somente visualizador da lista
  de reprodução do Studio): anuncia os comentários da faixa, se houver.
* Alt+NVDA+0 na janela do Studio: Abre o diálogo de configuração do
  complemento do Studio.
* Alt+NVDA+P na janela do Studio: abre o diálogo de perfis de transmissão —
  broadcast — do Studio.
* Alt+NVDA+F1: abre o diálogo de boas-vindas.

## Comandos não atribuídos

Os comandos a seguir não são atribuídos por padrão; se desejar atribuí-los,
use o diálogo Definir comandos — Gestos de entrada — para adicionar comandos
personalizados. Para fazer isso, na janela do Studio, abra o menu NVDA,
Preferências e Definir comandos. Expanda a categoria StationPlaylist,
localize os comandos não atribuídos na lista abaixo e selecione "Adicionar"
e digite o comando — gesto — que deseja usar.

* Mudar para a janela SPL Studio a partir de qualquer programa.
* Camada de controlador SPL.
* Anúncio do status do Studio, como reprodução de faixa a partir de outros
  programas.
* Anúncio do status da conexão do codificador a partir de qualquer programa.
* Camada Assistente SPL do SPL Studio.
* Anuncia o tempo incluindo segundos, do SPL Studio.
* Anúncio da temperatura.
* Anúncio do título da próxima faixa, se programada.
* Anúncio do título da faixa atualmente em reprodução.
* Marcando a faixa atual para o início da análise do tempo da faixa.
* Executando análise de tempo da faixa.
* Tira instantâneos — snapshots — da lista de reprodução.
* Localiza texto em colunas específicas.
* Localiza faixas com duração dentro de um determinado intervalo por meio do
  localizador de intervalo de tempo.
* Habilita ou desabilita o fluxo — streaming — de metadados rapidamente.

## Comandos adicionais ao usar codificadores

Os seguintes comandos estão disponíveis ao usar codificadores — encoders:

* F9: conecte o codificador selecionado.
* F10 (somente codificador SAM): Desconecte o codificador selecionado.
* Control+F9: Conecte todos os codificadores.
* Control+F10 (somente codificador SAM): Desconecte todos os codificadores.
* F11: Alterna se o NVDA mudará para a janela do Studio para o codificador
  selecionado se conectado.
* Shift+F11: Define se o Studio reproduzirá a primeira faixa selecionada
  quando o codificador estiver conectado a um servidor de fluxo — streaming.
* Control+F11: Alterna o monitoramento em segundo plano do codificador
  selecionado.
* Control+F12: abre um diálogo para selecionar o codificador que você
  excluiu (para realinhar os rótulos e as configurações do codificador).
* Alt+NVDA+0 e F12: Abre o diálogo de configurações do codificador para
  configurar opções como o rótulo do codificador.

Além disso, comandos de revisão/exploração de coluna estão disponíveis,
incluindo:

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

Os comandos disponíveis são:

* A: Automatização.
* C (Shift+C no leiaute JAWS): Título para a faixa atualmente em reprodução.
* C (leiaute JAWS): Alternar explorador de carrinho (somente visualizador de
  lista de reprodução).
* D (R no leiaute JAWS): Duração restante para a lista de reprodução (se uma
  mensagem de erro for dada, mova para o visualizador da lista de reprodução
  e, em seguida, execute este comando).
* E: Status de fluxo de metadados.
* Shift+1 a Shift+4, Shift+0: status para URLs de fluxo — streaming — de
  metadados individuais (0 é para codificador DSP).
* F: Localizar faixa (somente visualizador da lista de reprodução).
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
* Shift+F1: Abre o guia do usuário online.

## Controlador SPL

O Controlador SPL é um conjunto de comandos em camadas que você pode usar
para controlar o SPL Studio de qualquer lugar. Pressione o comando da camada
Controlador SPL e o NVDA dirá, "Controlador SPL". Pressione outro comando
para controlar várias configurações do Studio, como ligar/desligar o
microfone ou reproduzir a próxima faixa.

Os comandos do Controlador SPL disponíveis são:

* P: reproduz a próxima faixa selecionada.
* U: pausa ou retoma a reprodução.
* S: Para a faixa com enfraquecimento — fade out.
* T: Parada instantânea.
* M: Liga o microfone.
* Shift+M: Desliga o microfone.
* A: Ativa a automatização.
* Shift+A: Desativa a automatização.
* L: Ativa entrada de linha.
* Shift+L: Desativa a entrada de linha.
* R: Tempo restante para a faixa atualmente em reprodução.
* Shift+R: Progresso da varredura da biblioteca.
* C: Título e duração da faixa atualmente em reprodução.
* Shift+C: Título e duração da próxima faixa, se houver.
* E: Status de conexão do codificador.
* I: Contagem de ouvintes.
* Q: Informações de status do Studio, como se uma faixa está sendo
  reproduzida, se o microfone está ativado e outros.
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
ano, álbum, gênero, modo). Para o editor de lista de reprodução no Creator e
cliente Remote VT, os dados da coluna dependem da ordem das colunas,
conforme mostrada na tela. No Studio, lista de faixas principal do Creator,
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

Na janela do studio, você pode pressionar Alt+NVDA+0 para abrir o diálogo de
configuração do complemento. Alternativamente, vá ao menu de preferências do
NVDA e selecione o item Configurações do SPL Studio. Este diálogo também é
usado para gerenciar perfis de transmissão — broadcast.

## Diálogo de perfis de transmissão

Você pode salvar as configurações de programas específicos em perfis de
transmissão — broadcast. Esses perfis podem ser gerenciados por meio do
diálogo de perfis de transmissão SPL, que pode ser acessado pressionando
Alt+NVDA+P na janela do Studio.

## Modo tátil SPL

Se você estiver usando o Studio em um computador com tela sensível ao toque
com Windows 8 ou posterior e tiver o NVDA 2012.3 ou posterior instalado,
poderá executar alguns comandos do Studio a partir da tela de
toque. Primeiro, toque com três dedos para alternar para o modo SPL e, em
seguida, use os comandos de toque listados acima para executar os comandos.

## Versão 21.06

* O NVDA não fará mais nada ou reproduzirá tons de erro ao tentar abrir
  várias caixas de diálogo do complemento, como o diálogo de configurações
  do codificador. Esta é uma correção crítica necessária para oferecer
  suporte ao NVDA 2021.1.
* O NVDA não parecerá mais não fazer nada ou reproduzir tons de erro ao
  tentar anunciar o tempo completo (horas, minutos, segundos) do Studio
  (comando não atribuído). Isso afeta o NVDA 2021.1 ou posterior.

## Versão 21.04/20.09.7-LTS

* 21.04: NVDA 2020.4 ou posterior é requerido.
* Nos codificadores, o NVDA não falha mais em anunciar as informações de
  data e hora ao executar o comando de data/hora (NVDA+F12). Isso afeta o
  NVDA 2021.1 ou posterior.

## Versão 21.03/20.09.6-LTS

* O requisito mínimo de versão do Windows agora está vinculado às versões do
  NVDA.
* Removido o comando de e-mail de feedback (Alt+NVDA+Hífen). Por favor envie
  comentários para desenvolvedores de complementos usando as informações de
  contato fornecidas pelo Gerenciador de complementos.
* 21.03: partes do código-fonte do complemento agora incluem anotações de
  tipo.
* 21.03: tornou o código do complemento mais robusto com a ajuda do Mypy (um
  verificador de tipo estático do Python). Em particular, corrigiu várias
  falhas de longa data, como o NVDA não ser capaz de redefinir as
  configurações de complemento para os padrões em algumas circunstâncias e
  tentar salvar as configurações do codificador quando não
  carregado. Algumas correções de falhas proeminentes também foram portadas
  para 20.09.6-LTS.
* Corrigidas várias falhas com o diálogo de boas-vindas do complemento
  (Alt+NVDA+F1 na janela do Studio), incluindo várias caixas de diálogo de
  boas-vindas sendo mostradas e o NVDA parecendo não fazer nada ou
  reproduzindo tons de erro quando o diálogo de boas-vindas permanece aberto
  após o Studio sair.
* Corrigidas várias falhas com o diálogo de comentários de faixa (Alt+NVDA+C
  três vezes numa faixa no Studio), incluindo um tom de erro ouvido ao
  tentar salvar comentários e muitas caixas de diálogo de comentário de
  faixa que aparecem se Alt+NVDA+C for pressionado muitas vezes. Se o
  diálogo de comentários da faixa ainda for exibida após o Studio ser
  fechado, os comentários não serão salvos.
* Vários comandos de coluna, como o explorador de colunas
  (Control+NVDA+linha numérica) nas faixas do Studio e anúncios de status do
  codificador, não fornecem mais resultados errôneos quando executados após
  o NVDA ser reiniciado enquanto o foco está em faixas ou
  codificadores. Isso afeta o NVDA 2020.4 ou posterior.
* Corrigidos vários problemas com os instantâneos da lista de reprodução
  (Assistente SPL, F8), incluindo a incapacidade de obter dados do
  instantâneo e relatar faixas erradas como faixas mais curtas ou mais
  longas.
* O NVDA não anunciará mais "0 itens na biblioteca" quando o Studio sair no
  meio de uma varredura da biblioteca.
* O NVDA não falhará mais em salvar as alterações nas configurações do
  codificador depois que forem encontrados erros ao carregar as
  configurações do codificador e, subsequentemente, as configurações forem
  redefinidas para os padrões.

## Versão 21.01/20.09.5-LTS

A versão 21.01 suporta SPL Studio 5.30 e posterior.

* 21.01: NVDA 2020.3 ou posterior é requerido.
* 21.01: a configuração de inclusão do cabeçalho da coluna das configurações
  do complemento foi removida. A configuração do cabeçalho da coluna de
  tabela do próprio NVDA controlará os anúncios do cabeçalho da coluna em
  toda a suíte SPL e codificadores.
* Adicionado um comando para alternar entre tela versus inclusão de coluna
  personalizada e configuração de pedido (NVDA+V). Observe que este comando
  está disponível apenas quando focalizado numa faixa no visualizador de
  lista de reprodução do Studio.
* A ajuda da camada Assistente SPL e Controlador será apresentada como um
  documento do modo de navegação em vez de um diálogo.
* O NVDA não irá mais parar de anunciar o andamento da varredura da
  biblioteca se configurado para anunciar o progresso da varredura ao usar
  uma linha braille.

## Versão 20.11.1/20.09.4-LTS

* Suporte inicial para a suíte StationPlaylist 5.50.
* Melhorias na apresentação de vários diálogos do complemento graças aos
  recursos do NVDA 2020.3.

## Versão 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 ou posterior é requerido.
* 20.11: Resolvidos mais problemas de estilo de codificação e possíveis
  falhas com o Flake8.
* Corrigidos vários problemas com a caixa de diálogo de boas-vindas do
  complemento (Alt+NVDA+F1 do Studio), incluindo comando incorreto mostrado
  para feedback do complemento (Alt+NVDA+Hífen).
* 20.11: O formato de apresentação de coluna para itens de faixa e
  codificador na suíte StationPlaylist (incluindo o codificador SAM) agora é
  baseado no formato de item de lista SysListView32.
* 20.11: O NVDA agora anunciará informações de coluna para faixas em toda a
  suíte SPL independentemente da configuração de "anunciar descrições dos
  objetos" no painel de configurações de apresentação de objetos do
  NVDA. Para obter a melhor experiência, deixe esta configuração ativada.
* 20.11: No visualizador de lista de reprodução do Studio, a ordem das
  colunas personalizadas e a configuração de inclusão afetarão como as
  colunas das faixas são apresentadas ao usar a navegação de objetos para
  mover entre as faixas, incluindo o anúncio do objeto de navegação atual.
* Se o anúncio da coluna vertical for definido com um valor diferente de
  "qualquer coluna que estou revisando", o NVDA não anunciará mais dados
  incorretos da coluna após alterar a posição da coluna na tela via mouse.
* apresentação melhorada das transcrições da lista de reprodução (Assistente
  SPL, Shift+F8) ao visualizar a transcrição em tabela HTML ou formato de
  lista.
* 20.11: Nos codificadores, os rótulos dos codificadores serão anunciados ao
  executar comandos de navegação de objetos, além de pressionar as teclas de
  seta para cima ou para baixo para mover entre os codificadores.
* Em codificadores, além de Alt+NVDA+0 da linha numérica, pressionar F12
  também abrirá a caixa de diálogo de configurações do codificador para o
  codificador selecionado.

## Versão 20.10/20.09.2-LTS

* Devido a alterações no formato do arquivo de configurações do codificador,
  a instalação de uma versão mais antiga deste complemento após a instalação
  desta versão causará um comportamento imprevisível.
* Não é mais necessário reiniciar o NVDA com o modo de registrar depuração
  para ler as mensagens de debug do visualizador de log. Você pode ver as
  mensagens de depuração se o grau do log estiver definido como "depurar" no
  painel de configurações gerais do NVDA.
* No visualizador da lista de reprodução do Studio, o NVDA não incluirá
  cabeçalhos de coluna se esta configuração for desabilitada nas
  configurações do complemento e a ordem das colunas personalizadas ou
  configurações de inclusão não forem definidas.
* 20.10: a configuração de inclusão do cabeçalho da coluna nas configurações
  do complemento está obsoleta e será removida em uma versão futura. No
  futuro, a configuração do cabeçalho da coluna de tabela do próprio NVDA
  controlará os anúncios do cabeçalho da coluna em toda a suíte SPL e
  codificadores.
* Quando o SPL Studio está minimizado na bandeja do sistema (área de
  notificação), o NVDA anunciará este fato ao tentar mudar para o Studio de
  outros programas através de um comando dedicado ou como resultado de uma
  conexão de codificador.

## Versão 20.09-LTS

A versão 20.09.x é a última série de lançamento a suportar o Studio 5.20 e
baseada em tecnologias antigas, com versões futuras suportando o Studio 5.30
e recursos mais recentes do NVDA. Alguns novos recursos serão portados para
20.09.x, se necessário.

* Devido a mudanças no NVDA, a opção de linha de comando
  --spl-configvolatile não está mais disponível para tornar as configurações
  do complemento somente leitura. Você pode emular isto desmarcando a caixa
  de seleção "Salvar configurações ao sair do NVDA" no painel de
  configurações gerais do NVDA.
* Removida a configuração de recursos piloto da categoria Configurações
  Avançadas nas configurações do complemento (Alt+NVDA+0), usado para
  permitir que os usuários de instantâneos — snapshot — de desenvolvimento
  testem o código mais recente.
* Os comandos de navegação de coluna no Studio agora estão disponíveis em
  listas de faixas encontradas em solicitações de ouvinte, inserir faixas e
  outras telas.
* Vários comandos de navegação de coluna se comportarão como os próprios
  comandos de navegação de tabela do NVDA. Além de simplificar esses
  comandos, traz benefícios como facilidade de uso por usuários baixa visão.
* Os comandos de navegação em coluna vertical (Control+Alt+seta pra
  cima/baixo) agora estão disponíveis para o Creator, editor de lista de
  reprodução, Remote VT e Ferramenta de Faixa.
* O comando do visualizador de colunas de faixa (Control+NVDA+hífen) agora
  está disponível no Editor de Lista de Reprodução do Creator e no Remote
  VT.
* O comando do visualizador de colunas de faixa respeitará a ordem das
  colunas exibidas na tela.
* Em codificadores SAM, a capacidade de resposta do NVDA melhorada ao
  pressionar Control+F9 ou Control+F10 para conectar ou desconectar todos os
  codificadores, respectivamente. Isso pode resultar em maior verbosidade ao
  anunciar as informações do codificador selecionado.
* Em codificadores SPL e AltaCast, pressionar F9 agora conectará o
  codificador — encoder — selecionado.

## Versões mais antigas

Por favor, consulte o link do changelog para notas de lançamento para
versões de complemento antigas.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
