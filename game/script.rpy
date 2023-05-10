

define p = Character("Peixoto")
define l = Character("Lilas")

#imagens do jogo

image APeixoto="astronautaPeixoto.png"
image ALilas="astronautaLilas.png"
image APeixotoB="APeixotoB.png"
image ALilasB="ALilasB.png"
image Espaco="Espaço.jpg"
image Espaco2="Espaço2.png"



label start:

   
    scene Espaco

    show ALilas at left
    show APeixoto at right


    p"Eai rapaz, como ta as coisas"
    l"Sabe como é né com cabeça no espaço"
    "Os dois riram"
    p"Oque você tem ai, dessa vez?"

    hide ALilas

    show ALilasB at left
    "Lilas mostra um botão veremlho"


    hide ALilasB
    hide APeixoto

menu:

    "Peixoto aperta o botão":
        jump ap

    "Lila aperta o botão":
        jump al 




label ap:


    scene Espaco

    show ALilasB at left
    show APeixoto at right

    l"NÃO SEI OQUE É, E NEM OQUE FAZ!"
    hide ALilasB
    hide APeixoto


    show ALilas at left
    show APeixotoB at right
    p"Da aqui, deixa eu ver"
    "Peixoto aberta o botão"

    hide ALilas


    scene Espaco2
    show ALilas at left
    show APeixotoB at right

    p"Não houve nada, que bosta, mas é isso. Tchau Lilas"
    l"Tchau peixoto!"
    
    hide APeixotoB
    hide ALilas

    show ALilasB at left



    "Lilas se vira, ao sentir um pulso passando por ele..."
    l"Mais que por..."

    hide ALilasB


    
  

    return

    




label al:



    scene Espaco

    show ALilasB at left
    show APeixoto at right

    l"NÃO SEI OQUE É, E NEM OQUE FAZ! QUER TESTAR?"
    "Peixoto tem sujeira aqui para você limpar, câmbio!"
    p"Queria mais não posso, não tenho mais tempo, é isso tchau! "
    hide APeixoto
    l"Tchau!"
    "Lilas olhou para o botão e o apertou"

    scene Espaco2 

    show ALilasB at left
    
    "Ele sentiu um leve pulso passando por ele, assim se vira..."
    l"Mais que por..."

    hide ALilasB
    hide APeixoto


    return










    
   

    


    
