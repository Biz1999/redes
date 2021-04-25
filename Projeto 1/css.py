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
                    padding: 1rem;
                    display: flex;
                    flex-direction: column;
                    align-items:center;
                    justify-content: center;
                    border-style: solid;
                    color:#8630a8;
                    background-color: #fff;
                }}

                .grid:hover{{
                    transform: scale(1.1);
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

            </style>