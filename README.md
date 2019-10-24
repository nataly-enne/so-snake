# Snake
Conceitos de gerenciamento de IO e networking IO em uma aplicação com interface gráfica.

# What is it?
A aplicação a ser desenvolvida foi batizada de PySnakes (em homenagem ao jogo da cobrinha), pois nesse caso, teremos múltiplas
snakes em um mesmo tabuleiro. No jogo, múltiplas snakes podem estar no mesmo ao mesmo tempo.

### Cenário 1 – I/O programada
O cenário implementado foi o de I/O programada. Nesse cenário o servidor deve configurar os sockets de forma não bloqueante e deve tratar todas as entradas, saídas e processamento em uma thread única.

#### Para compilar o programa, vá ao diretorio do arquivo e em um terminal execute o `server.py`
```bash
 python3 server.py 
```

#### Em um outro terminal, inicie `client.py` com a seguinte linha de código:
```bash
 python3 client.py 
```

#### Caso aconteça um erro na biblioteca <i>pygame</i>, execute:
```bash
python3 -m pip install pygame
```

## Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/nataly-enne">
        <img src="https://avatars3.githubusercontent.com/u/26802307?s=400&v=4" width="100px;" alt="Nátaly Enne"/>
        <br />
        <sub><b>Nátaly Enne</b></sub>
      </a><br />
      <a href="https://github.com/nataly-enne/s0-snake/commits?author=nataly-enne" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/Vanz5">
        <img src="https://avatars2.githubusercontent.com/u/36575665?s=400&v=4" width="100px;" alt="Van Allem"/>
        <br />
        <sub><b>Van Allem</b></sub>
      </a><br />
      <a href="https://github.com/nataly-enne/so-snake/commits?author=Vanz5" title="Code">💻</a>
    </td>
  </tr>
</table>
