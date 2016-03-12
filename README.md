# garupa.com

Sistema web de caronas solidárias para associados a UFCG.
Desenvolvido por Arthur Emanuel, Arthur Vinícius, Jeferson Silva, Marianne Linhares e Victor Andrade para a disciplina de SI1 no período 2015.2
na UFCG.

## Primeira entrega - como visualisar as páginas ?

Para a primeira entrega usamos: html, js, css, angular.js e alguns frameworks e librarys (bootstrap, jquery, entre outros).

Para acessar as telas deve-se:
- Fazer git clone do projeto

  `git clone https://github.com/mari-linhares/garupa.com`

- Na pasta do projeto levantar um servidor local.
  Há vários modos de fazer isso, algumas opções:
	- Pode-se usar uma IDE que faz isso para você, como o [webstorm](https://www.jetbrains.com/webstorm/).
	- Usar o [python SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html) para levantar o server.
		Na pasta do garupa.com execute:

		`$python -m SimpleHTTPServer`

		A página estará disponível em localhost:8000

Pronto! A página agora está disponível.

### Como interagir com as telas

A primeira tela é a tela que fala sobre o site que leva para a tela de cadastro, caso erre a senha o usuario sera levado a tela de login.
Para acessar a tela principal preencha apenas o campo matricula com alguma informação. Exemplo: 'dilma'.

Para a primeira entrega criamos 3 usuários de teste: Dilma, Einstein e Safadão. Você está logado como Dilma, mas pode acessar
os perfis de Einstein e Safadão respectivamente nos seguintes endereços:
http://localhost:8000/#/perfil/einstein e http://localhost:8000/#/perfil/safadao.

A tela de perfil é a tela principal, nela encontramos um calendário com as caronas semanais do usuário, ou seja essas caronas
se repetem toda semana. Mas também temos uma tabela com as caronas agendadas, essas caronas não se repetem.

Ainda na tela do perfil ao lado de caronas agendadas você tem a opção de oferecer uma carona ou buscar uma carona.
Ao clicar em qualquer um desses botões você irá ser redirecionado para uma nova tela.

Na tela de oferecer carona você poderá definir se está indo para UFCG ou voltando da UFCG, a rota que irá fazer, entre outras informações.

Na tela de buscar carona você pode procurar caronas que se enquadram com suas informações (a ideia é o campo de bairro ser preenchido
automaticamente com o bairro que o usuário cadastrou, porém ainda podendo ser alterado). Caso não exista nenhuma carona do tipo que o usuário
estiver buscando ele pode pedir para ser notificado quando uma carona desse tipo surgir. Para visualiação nesta entrega o filtro funciona apenas 		por bairro. O usuário Einstein mora no Catole para fins de teste.
Ao achar as caronas baseando-se no filtro o usuário pode contactar o motorista da carona para pegar uma vaga no carro.
O motorista será notificado do interesse na carona.


## Primeira entrada - comentários a respeito das US's

US 01 - “Como um possível usuário do sistema, gostaria de efetuar o cadastro como motorista e/ou passageiro.”
	Resumidamente, o que é necessário fazer para essa US é uma tela de cadastro, contendo duas opções de conta: motorista e passageiro, e pra cada tipo de conta alguns dados precisam ser fornecidos no ato do cadastro.
	Como tratamos essa US: Desenvolvemos uma tela de cadastro, que no nosso caso está na tela principal do site (home.html). Nesta tela disponibilizamos a opção de escolher o tipo da conta, e solicitamos os mesmos dados para o cadastro dos dois tipos, pois todos vão ser utilizados nos dois casos.

US 02 - “Como um motorista devo cadastrar o meu horário de partida, bem como o horário e o endereço de retorno - caso este endereço seja diferente do cadastrado - para que potenciais passageiros possam visualizar a disponibilidade de vaga.”
	Resumidamente, o que é necessário fazer para essa US é disponibilizar a um usuário do tipo motorista a opção de cadastrar horários de partida e de retorno, para que outros possam visualizar horários em que caronas estão sendo oferecidas.
	Como tratamos essa US: Desenvolvemos uma tela onde usuários que tenham conta do tipo motorista podem oferecer carona (offering.html). Nesta tela o motorista pode registrar horários recorrentes (semanalmente) ou um horário único, no qual ele estará disposto a oferecer caronas. Além disso, o motorista pode marcar os bairros pelos quais ele irá passar, facilitando a busca de carona por parte dos passageiros.

US 03 - “Como um motorista gostaria de visualizar as informações do bairro e do horário do passageiro para então poder aceitar ou não a solicitação.”
	Resumidamente, o que é necessário fazer para essa US é, no caso de um passageiro fazer o pedido de uma carona, disponibilizar para o motorista as informações da carona (horário, data, bairro, dados do passageiro) e dar ao motorista a opção de aceitar ou recusar o pedido.
	Como tratamos essa US: Desenvolvemos uma tela de notificações (notifications.html). Nesta tela os usuários têm acesso às informações de caronas solicitadas, pedidos aceitos ou negados. Esta tela de notificações trata dessa US, já que no caso de notificações de caronas solicitadas, ela disponibiliza as informações do pedido e as opções de aceitação ou reprovação.

US 04 - “Como um motorista quero aceitar ou recusar um pedido de carona.”
	Essa US é uma parte da US 03, logo, foi tratada da mesma maneira, através da tela de notificações (notifications.html).

US 05 - “Como um passageiro devo cadastrar o meu horário de partida, bem como o horário e o endereço de retorno, caso este endereço seja diferente do cadastrado.”
	Resumidamente, o que é necessário fazer para essa US é disponibilizar a um usuário do tipo passageiro a opção de cadastrar horários de partida e de retorno.
	Como tratamos essa US: Desenvolvemos uma tela de perfil para os usuários (profile.html), e nela o passageiro tem a opção de cadastrar horários nos quais ele desejará carona.

US 06 - “Como um passageiro gostaria de ver quais os motoristas com o mesmo endereço (bairro) e horário de partida que eu.”
	Resumidamente, o que é necessário fazer para essa US é permitir a um usuário do tipo passageiro a busca de motoristas de determinado bairro que estejam oferecendo carona para a UFCG no horário desejado pelo passageiro.
	Como tratamos essa US: Desenvolvemos uma tela de busca de caronas (search-rides.html), e nela um usuário do tipo passageiro pode buscar por caronas que estão sendo oferecidas. A busca filtra as caronas disponíveis em relação ao bairro, dia e horário da carona desejada, mostrando os motoristas que oferecem a carona e dando ao passageiro a opção de pedir carona a algum.
US 07 -  “Como um passageiro gostaria de ver quais os motoristas com o mesmo
endereço (bairro) de destino e horário de retorno que eu.”
	Resumidamente, o que é necessário fazer para essa US é permitir a um usuário do tipo passageiro a busca de motoristas de determinado bairro que estejam saindo da UFCG no horário desejado pelo passageiro.
	Como tratamos essa US: Essa US é tratada da mesma maneira que a anterior, a partir da tela (search-rides.html), pois nela o passageiro informa se a carona desejada é para a UFCG ou saindo da UFCG.

US 08 - “Como um passageiro gostaria de agendar uma carona.”
	US tratada de maneira semelhante as US 06 e 07.

Extras:

1. Desenvolvemos telas para edição de informações da conta e recuperação de conta.

2. Desenvolvemos telas que possibilitam interação social entre os usuários do site, adicionando amigos, conversando com outros usuários e avaliando outros usuários.
