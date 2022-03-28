#Este programa tem como finalidade criar um script que diga se sua senha é forte
#! python
import re
# PASSO 1: PEDIR PARA INSERIR A SENHA
senhaRegex = re.compile(r'^(((?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%<^&*?])[a-zA-Z0-9!@#$%<^&*?]{8,})|([a-zA-Z]+([- .,_][a-zA-Z]+){4,}))$')
insenha = input('Por favor insira sua senha e iremos ver se ela é forte O7 ')
# PASSO 2: CONFERIR A SENHA


matches=[]
if senhaRegex.findall(insenha):
    print('A senha é potente patrão, pode por fé ')
else:
     print('xiii patrão sua senha e fraca') 