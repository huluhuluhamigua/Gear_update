fr_prompt_lleqa = {
    'key':[
        'example_doc_1','example_doc_2',
        'example_doc_1_queries','example_doc_2_queries',
        'target_doc','num_q'
    ],
    'prompt': \
'''J'ai un document cible et j'ai besoin que tu prévois {num_q} questions basées sur ce document. Veuillez vous assurer que :
1. Les questions couvrent les informations clés et différentes parties du document ;
2. Il y a une variété de types de questions, allant des simples vérifications de faits aux questions nécessitant une analyse approfondie ;
3. Les questions ne se répètent pas, chaque question cible un point d'information différent du document ;
4. Les questions sont formulées en français, avec clarté et précision ;
5. Prenez en compte le niveau de difficulté des questions, allant des questions de base aux questions plus difficiles.

Voici quelques exemples de documents et de questions basées sur ces documents, à titre de référence :

[Exemple de document] {exemple_doc_1}
[Questions basées sur le document]
{exemple_doc_1_reponses}

[Exemple de document] {exemple_doc_2}
[Questions basées sur le document]
{exemple_doc_2_reponses}

Maintenant, veuillez poser des questions basées sur le document cible suivant :

[Document cible] {document_cible}
[Questions basées sur le document]
'''   
} 
