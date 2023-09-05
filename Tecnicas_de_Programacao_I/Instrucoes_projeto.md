## Projeto de Técnicas de Programação I

Você trabalha em uma consultoria de dados que foi contratada para realizar a distribuição de materiais didáticos nas escolas da cidade do Rio de Janeiro. Sua missão é realizar tratamentos nos dados de acordo com as normas de padrão definidas pelo cliente e encontrar qual a melhor rota que um caminhão deve realizar para entregar os materiais didáticos de forma a otimizar o seu percurso.

#### Para esse projeto você recebeu três arquivos:

<li> 
escolas.csv: contém os dados das escolas. Baixe o dataset aqui;
<li>
subprefeituras.csv: contém dados de quais bairros pertem a cada subprefeitura. Baixe o dataset aqui;
<li>
material_didatico.csv: contém a quantidade de material didático que cada escola deve receber. Baixe o dataset aqui.
</li>

#### Como produto final, você deve entregar:

<li>
um arquivo csv no qual as linhas já estarão ordenas de acordo com a rota a ser seguida. Além disso, os dados devem estar no padrão especificado abaixo e contendo as seguintes colunas: id da escola, nome da escola, tipo da escola (EM, CIEP ou colégio), logradouro da entrega, número, bairro, subprefeitura, latitude, longitude e quantidade de mat erial didático que deve ser entregue. O logradouro da escola deve estar em uma coluna diferente do número;
<li>
um arquivo csv com a quantidade total de material escolar por subprefeitura para que sejam contabilizados os custos por subprefeitura
</li>

#### Como padrão dos dados, considere:

<li>
nome das colunas em snake_case
<li>
strings não devem conter acentos
<li>
todas as strings devem estar em maiúsculo
<li>
padronização do nome dos logradouros sem abreviação (Ex: R. deve estar como Rua)
<li>
latitude e longitude devem conter apenas 5 casas decimais
<li>
os ids da escola devem todos ser strings com 3 caracteres (Ex: '024')
</li>

#### Desafio:

Entregar um plot com a representação da melhor rota que você encontrou, por exemplo:

![exemplo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FOptimized-delivery-routes-of-the-perishable-food-products_fig5_317177111&psig=AOvVaw35vg_R0o3btr3s8B0AoUP2&ust=1694006355302000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCIiJzMrHk4EDFQAAAAAdAAAAABAE)

Obs: O otimizador não é a parte mais importante do projeto. Foque no tratamento dos dados e se preciso, pode reduzir a quantidade de escolas para rodar o otimizador.