from datetime import datetime

def separaNomes(nomes):
    tabela = f'''
            <tr style="width:100%">
                <th>Nome</th>
                <th>Sobrenome</th>
            </tr>
    '''
    for i in range (len(nomes)):
        tabela+=f'''
            <tr style="text-align:center">
                <td>{ nomes[i][0] }</td>
                <td>{ nomes[i][1] }</td> 
            </tr>
        '''
    return tabela


def sendPage( nomes, error ):
    # data e horário
    date = (f'{datetime.now():%m-%Y %H:%M}')

    #código da página
    page = f'''
        <!DOCTYPE HTML>\n
        <html> 
        <head>
            <link rel="shortcut icon" href="#">
            <style type="text/css">
            :root {{
                --omrs-color-ink-lowest-contrast: rgba(47, 60, 85, 0.18);
                --omrs-color-ink-low-contrast: rgba(60, 60, 67, 0.3);
                --omrs-color-ink-medium-contrast: rgba(19, 19, 21, 0.6);
                --omrs-color-interaction: #1e4bd1;
                --omrs-color-interaction-minus-two: rgba(73, 133, 224, 0.12);
                --omrs-color-danger: #b50706;
                --omrs-color-bg-low-contrast: #eff1f2;
                --omrs-color-ink-high-contrast: #121212;
                --omrs-color-bg-high-contrast: #ffffff;
                
            }}
            /** END: Non Openmrs CSS **/
            div.omrs-input-group {{
            margin-bottom: 1.5rem;
            position: relative;
            width: 20.4375rem;
            }}

            /* Input*/
            .omrs-input-underlined > input,
            .omrs-input-filled > input {{
                border: none;
                border-bottom: 0.125rem solid var(--omrs-color-ink-medium-contrast);
                width: 100%;
                height: 2rem;
                font-size: 1.0625rem;
                padding-left: 0.875rem;
                line-height: 147.6%;
                padding-top: 0.825rem;
                padding-bottom: 0.5rem;
            }}

            .omrs-input-underlined > input:focus,
            .omrs-input-filled > input:focus {{
                outline: none;
            }}

            .omrs-input-underlined > .omrs-input-label,
            .omrs-input-filled > .omrs-input-label {{
                position: absolute;
                top: 0.9375rem;
                left: 0.875rem;
                line-height: 147.6%;
                color: var(--omrs-color-ink-medium-contrast);
                transition: top .2s;
            }}

            .omrs-input-underlined > svg,
            .omrs-input-filled > svg {{
                position: absolute;
                top: 0.9375rem;
                right: 0.875rem;
                fill: var(--omrs-color-ink-medium-contrast);
            }}

            .omrs-input-underlined > .omrs-input-helper,
            .omrs-input-filled > .omrs-input-helper {{
                font-size: 0.9375rem;
                color: var(--omrs-color-ink-medium-contrast);
                letter-spacing: 0.0275rem;
                margin: 0.125rem 0.875rem;
            }}

            .omrs-input-underlined > input:hover,
            .omrs-input-filled > input:hover {{
                background: var(--omrs-color-interaction-minus-two);
                border-color: var(--omrs-color-ink-high-contrast);
            }}

            .omrs-input-underlined > input:focus + .omrs-input-label,
            .omrs-input-underlined > input:valid + .omrs-input-label,
            .omrs-input-filled > input:focus + .omrs-input-label,
            .omrs-input-filled > input:valid + .omrs-input-label {{
                top: 0;
                font-size: 0.9375rem;
                margin-bottom: 32px;;
            }}

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus + .omrs-input-label,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus + .omrs-input-label {{
                color: var(--omrs-color-interaction);
            }}

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus {{
                border-color: var(--omrs-color-interaction);
            }}

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus ~ svg,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus ~ svg {{
                fill: var(--omrs-color-ink-high-contrast);
            }}

            /** DISABLED **/

            .omrs-input-underlined > input:disabled {{
                background: var(--omrs-color-bg-low-contrast);
                cursor: not-allowed;
            }}

            .omrs-input-underlined > input:disabled + .omrs-input-label,
            .omrs-input-underlined > input:disabled ~ .omrs-input-helper{{
                color: var(--omrs-color-ink-low-contrast);
            }}

            .omrs-input-underlined > input:disabled ~ svg {{
                fill: var(--omrs-color-ink-low-contrast);
            }}
            /** DANGER **/

            .omrs-input-underlined.omrs-input-danger > .omrs-input-label, .omrs-input-underlined.omrs-input-danger > .omrs-input-helper,
            .omrs-input-filled.omrs-input-danger > .omrs-input-label, .omrs-input-filled.omrs-input-danger > .omrs-input-helper{{
                color: var(--omrs-color-danger);
            }}

            .omrs-input-danger > svg {{
                fill: var(--omrs-color-danger);
            }}

            .omrs-input-danger > input {{
                border-color: var(--omrs-color-danger);
            }}

            .omrs-input-underlined > input {{
                background: var(--omrs-color-bg-high-contrast);
            }}
            .omrs-input-filled > input {{
                background: var(--omrs-color-bg-low-contrast);
            }}

            
            </style>
            <meta charset="utf-8">
            <title>Home</title>
        </head>
        <body>
            <h1>This is THE WEB PAGE</h1> 
            <br>
            Hello World!
            <img src='haruhi.jpg' width='100%' height='100%'>
            <form method='POST'>
                <div class='omrs-input-group'>
                    <label class="omrs-input-underlined">
                    <input type="text" name="fname" >
                    <span class="omrs-input-label">Nome</span>
                    <br>
                    </div>
                    <div class='omrs-input-group'>
                    <label class="omrs-input-underlined omrs-input-danger">
                    <br>
                    <input type="text" name="lname">
                    <span class="omrs-input-label">Sobrenome</span>
                    <br><br>
                    <input type="submit" value="Submit">
                </div>
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
    return (page if error==0 else page404)