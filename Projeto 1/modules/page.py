from datetime import datetime


def separaNomes(nomes):
    tabela = f'''
            <tr style="width:30%">
                <th>ID</th>
                <th>Nome</th>
                <th>Sobrenome</th>
            </tr>
    '''
    if nomes:
        for i in range(len(nomes)):
            tabela += f'''
                <tr style="text-align:center">
                    <td>      { i }    </td>
                    <td>{ nomes[i][0] }</td>
                    <td>{ nomes[i][1] }</td> 
                </tr>
            '''
    else:
        tabela +=f'''
            <tr style="text-align:center">
                <td>    null   </td>
                <td>    null   </td>
                <td>    null   </td>
            </tr>
        '''
    return tabela


def namesId (nomes):
    options=''
    if nomes:
        for i in range(len(nomes)):
            options+=f'<option value={i}>'
    else :
            options+=f'<option value=''>'
            options+=f'<option value=null>'
    
    return options


def sendPage(nomes, error):

    # data e horário
    date = (f'{datetime.now():%m-%Y %H:%M}')
    # código da página
    page = f'''<!DOCTYPE HTML>\n
        <html>
        <head>
            <title>Home</title>
            <meta name="viewport" charset="utf-8" content="width=device-width, initial-scale=1.0">
            <link rel="icon" href="data:;base64,iVBORw0KGgo=">
            <script>
                let btn = document.querySelector("button");

                btn.addEventListener("click", active);

                function active() {{
                btn.classList.toggle("is_active");
                }}
            </script>
            <style type="text/css">
                body {{
                display: flex;
                flex-direction: column;
                background: #0f2027; /* fallback for old browsers */
                background: linear-gradient(to right,#a145c5, #571874, #2f0244);
                font-family: 'Roboto', sans-serif;
                color: #fff;
                }}

                .grid{{ 
                    margin: auto;
                    padding: 2rem;
                    flex:1
                    flex-direction: column;
                    align-items:center;
                    justify-content: center;
                    border-style: solid;
                    color:#8630a8;
                    background-color: #fff;
                }}

                .formTitle{{
                    text-align: center;
                }}

                .field__input{{ 
                --uiFieldPlaceholderColor: var(--fieldPlaceholderColor, #767676);
                
                background-color: transparent;
                border-radius: 0;
                border: none;

                -webkit-appearance: none;
                -moz-appearance: none;


                font-size: inherit;
                
                }}

                .field__input:focus::-webkit-input-placeholder{{
                color: var(--uiFieldPlaceholderColor);
                }}

                .field__input:focus::-moz-placeholder{{
                color: var(--uiFieldPlaceholderColor);
                }}

                /*
                =====
                CORE STYLES
                =====
                */

                .field{{
                --uiFieldBorderWidth: var(--fieldBorderWidth, 2px);
                --uiFieldPaddingRight: var(--fieldPaddingRight, 1rem);
                --uiFieldPaddingLeft: var(--fieldPaddingLeft, 1rem);   
                --uiFieldBorderColorActive: var(--fieldBorderColorActive, rgba(22, 22, 22, 1));

                display: var(--fieldDisplay, inline-flex);
                position: relative;
                font-size: var(--fieldFontSize, 1rem);
                width:100%;
                }}

                .field__input{{
                box-sizing: border-box;
                width: var(--fieldWidth, 100%);
                height: var(--fieldHeight, 3rem);
                padding: var(--fieldPaddingTop, 1.25rem) var(--uiFieldPaddingRight) var(--fieldPaddingBottom, .5rem) var(--uiFieldPaddingLeft);
                border-bottom: var(--uiFieldBorderWidth) solid var(--fieldBorderColor, rgba(0, 0, 0, .25));
                color: #8630a8;  
                }}

                .field__input:focus{{
                outline: none;
                }}

                .field__input::-webkit-input-placeholder{{
                opacity: 0;
                transition: opacity .2s ease-out;
                }}

                .field__input::-moz-placeholder{{
                opacity: 0;
                transition: opacity .2s ease-out;
                }}

                .field__input:focus::-webkit-input-placeholder{{
                opacity: 1;
                transition-delay: .2s;
                }}

                .field__input:focus::-moz-placeholder{{
                opacity: 1;
                transition-delay: .2s;
                }}

                .field__label-wrap{{
                box-sizing: border-box;
                pointer-events: none;
                cursor: text;

                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
                }}

                .field__label-wrap::after{{
                content: "";
                box-sizing: border-box;
                width: 100%;
                height: 0;
                opacity: 0;

                position: absolute;
                bottom: 0;
                left: 0;
                }}

                .field__input:focus ~ .field__label-wrap::after{{
                opacity: 1;
                }}

                .field__label{{
                position: absolute;
                left: var(--uiFieldPaddingLeft);
                top: calc(50% - .5em);

                line-height: 1;
                font-size: var(--fieldHintFontSize, inherit);

                transition: top .2s cubic-bezier(0.9, -0.15, 0.1, 1.15), opacity .2s ease-out, font-size .2s ease-out;
                will-change: bottom, opacity, font-size;
                }}

                .field__input:focus ~ .field__label-wrap .field__label,
                .field__input:not(:placeholder-shown) ~ .field__label-wrap .field__label{{
                --fieldHintFontSize: var(--fieldHintFontSizeFocused, .75rem);

                top: var(--fieldHintTopHover, .25rem);
                }}

                /* 
                effect 1
                */

                .field_v1 .field__label-wrap{{
                    overflow: hidden;
                }}

                .field_v1 .field__label-wrap::after{{
                border-bottom: var(--uiFieldBorderWidth) solid var(--uiFieldBorderColorActive);
                transition: opacity .2s ease-out;
                will-change: opacity;
                }}
                .field_v1 .field__input:focus ~ .field__label-wrap::after{{
                    transform: translate3d(0, 0, 0);
                    transition-delay: 0;
                }}

                /* 
                effect 2
                */

                .field_v2 .field__label-wrap{{
                overflow: hidden;
                }}

                .field_v2 .field__label-wrap::after{{
                border-bottom: var(--uiFieldBorderWidth) solid var(--uiFieldBorderColorActive);
                transform: translate3d(-105%, 0, 0);
                will-change: transform, opacity;
                transition: transform .285s ease-out .2s, opacity .2s ease-out .2s;
                }}

                .field_v2 .field__input:focus ~ .field__label-wrap::after{{
                transform: translate3d(0, 0, 0);
                transition-delay: 0;
                }}

                .field{{
                --fieldBorderColor: #D1C4E9;
                --fieldBorderColorActive: #673AB7;
                }}

                td,th{{
                    border: 1px solid #dddddd;
                    padding: 8px;
                }}
                .btn-submit{{
                    width:100%;
                    margin-top:10px;
                    align-items:center;
                    border-radius:10px;
                    border-color: #8630a8;
                    color: #8630a8;
                }}
                .btn-submit:hover{{
                    background: #8630a8;
                    color: #fff;
                }}
                
            </style>
        </head> 
        <body>
            <h1 style='text-align:center'>ESCOLHA UM DOS FORMULÁRIOS</h1> 
            <br>
            <br>
            <img src='haruhi.jpg' width="300" height="300">
            <div style='display:flex;width:100%;justify-content:space-around'>
                <div class='grid'>
                <label class='formTitle'><b>ADICIONA</b> pessoa</label>
                <form method='POST' autocomplete="off">
                    <label class="field field_v1">
                        <input class="field__input" placeholder="Islanzin" name="new_fname">
                        <span class="field__label-wrap">
                            <span class="field__label">Nome</span>
                        </span>
                    </label>
                    <br>
                    <label class="field field_v2">
                        <input class="field__input" placeholder="Silva" name="new_lname">
                        <span class="field__label-wrap">
                            <span class="field__label">Sobrenome</span>
                        </span>
                    </label>
                    <input type="submit" class="btn-submit" value="Submit">
                </form>
                </div>         
                <div class='grid'>
                <label class='formTitle'><b>ATUALIZA</b> pessoa</label>
                <form method='POST' autocomplete="off">
                    <label class="field field_v1">
                        <input class="field__input" list="ids" name='update_id' placeholder="ID">
                        <span class="field__label-wrap">
                            <span class="field__label">ID</span>
                        </span>
                        <datalist id="ids">
                            {namesId(nomes)}
                        </datalist>
                        
                    </label>
                    <label class="field field_v1">
                        <input class="field__input" placeholder="Islanzin" name="update_fname">
                        <span class="field__label-wrap">
                            <span class="field__label">Nome</span>
                        </span>
                    </label>
                    <br>
                    <label class="field field_v2">
                        <input class="field__input" placeholder="Silva" name="update_lname">
                        <span class="field__label-wrap">
                            <span class="field__label">Sobrenome</span>
                        </span>
                    </label>
                    <input type="submit" class="btn-submit" value="Submit">
                </form>
                </div>          
                <div class='grid'>
                <label class='formTitle'><b>DELETA</b> pessoa</label>
                <form method='POST' autocomplete="off">
                    <label class="field field_v1">
                        <input class="field__input" list="ids" name='delete_id' placeholder="ID">
                        <span class="field__label-wrap">
                            <span class="field__label">ID</span>
                        </span>
                        <datalist id="ids">
                            {namesId(nomes)}
                        </datalist>
                    </label>
                    <input type="submit" class="btn-submit" value="Submit">
                </form>
                </div>          
            </div>
            <div style="display:flex;align-items:center;justify-content:center;margin-top:2rem"> 
            <table style="width:50%;align: center;border-collapse: collapse;table-layout: fixed">
            {separaNomes(nomes)}
            </table>
            </div>
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
