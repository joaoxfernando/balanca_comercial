# Balança Comercial

Criei esse script basicamente para baixar automaticamente os arquivos de Importação e Exportação mais recentes para alimentar o <a href='https://app.powerbi.com/view?r=eyJrIjoiNWNlNTJlNTItYjBmMy00NGUwLWIxNWItMjc0MTdhYzUzZjg0IiwidCI6IjVjYzNlODFhLTVjNGUtNGFkOC1iMzMzLTc2ZDQxMTdmNGFlNSJ9' target='_blank'>Dashboard da Balança Comercial</a> 
Não sendo necessário entrar no site, baixar os arquivos e ainda localizar a pasta do projeto para salvá-los.

Basta indicar de qual ano deseja baixar o arquivo, se precisar de mais de um ano, pode rodar o script quantas vezes forem necessárias.
Se você estiver atualizando durante o ano corrente e já existir um arquivo com o mesmo nome, ele irá deletar o que já existe e baixar um novo arquivo.</p>

## Baixar arquivos 
- Primeiro, crie um arquivo **.env** com o diretório onde os arquivos ficam salvos. Eu separo uma pasta para as importações e outro para as exportações. O arquivo deve ter a seguinte estrutura: 
    * PATH_DIR=diretório
    <br>Onde o atributo **PATH_DIR** você deve deixar com esse nome e após o sinal de "=" você deve adicionar o diretório onde irá salvar os arquivos.
    * Se estiver utilizando windows, troque todas as barras \ por / no caminho do diretório