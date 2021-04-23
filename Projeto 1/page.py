from datetime import datetime


def separaNomes(nomes):
    tabela = f'''
            <tr style="width:100%">
                <th>Nome</th>
                <th>Sobrenome</th>
            </tr>
    '''
    for i in range(len(nomes)):
        tabela += f'''
            <tr style="text-align:center">
                <td>{ nomes[i][0] }</td>
                <td>{ nomes[i][1] }</td> 
            </tr>
        '''
    return tabela


def sendPage(nomes, error):

    # data e horário
    date = (f'{datetime.now():%m-%Y %H:%M}')

    # código da página
    page = f'''<!DOCTYPE HTML>\n<html> 
        <body>
            <h1>This is THE WEB PAGE</h1> 
            <br>
            Hello World!
            <img src="haruhi.jpg" height='30%' width='30%' />
            <form method='POST'>
                <label style='background-color:red'>Primeiro nome:</label><br>
                <input type="text" name="fname"><br>
                <label>Sobrenome:</label><br>
                <input type="text" name="lname"><br><br>
                <input type="submit" value="Submit">
            </form> 
            <br>{date}<br>
            <table style="width:100%">
            {separaNomes(nomes)}
            </table>
        </body>
        </html>\r\n\r\n'''

    page404 = '''<!DOCTYPE HTML>\n<html>
        <body>
            <h1>
            ERRO 404<br>Pagina nao encontrada
            </h1>
        </body>
        </html>\r\n\r\n'''
    return (page if error == 0 else page404)
