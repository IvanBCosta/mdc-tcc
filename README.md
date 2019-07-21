# Fruits-360
Content

The following fruits are included: Apples (different varieties: Crimson Snow, Golden, Golden-Red, Granny Smith, Pink Lady, Red, Red Delicious), Apricot, Avocado, Avocado ripe, Banana (Yellow, Red, Lady Finger), Cactus fruit, Cantaloupe (2 varieties), Carambula, Cherry (different varieties, Rainier), Cherry Wax (Yellow, Red, Black), Chestnut, Clementine, Cocos, Dates, Granadilla, Grape (Blue, Pink, White (different varieties)), Grapefruit (Pink, White), Guava, Hazelnut, Huckleberry, Kiwi, Kaki, Kohlrabi, Kumsquats, Lemon (normal, Meyer), Lime, Lychee, Mandarine, Mango, Mangostan, Maracuja, Melon Piel de Sapo, Mulberry, Nectarine, Orange, Papaya, Passion fruit, Peach (different varieties), Pepino, Pear (different varieties, Abate, Kaiser, Monster, Red, Williams), Pepper (Red, Green, Yellow), Physalis (normal, with Husk), Pineapple (normal, Mini), Pitahaya Red, Plum (different varieties), Pomegranate, Pomelo Sweetie, Quince, Rambutan, Raspberry, Redcurrant, Salak, Strawberry (normal, Wedge), Tamarillo, Tangelo, Tomato (different varieties, Maroon, Cherry Red, Yellow), Walnut.

Dataset properties

Total number of images: 71125.

Training set size: 53177 images (one fruit per image).

Test set size: 17845 images (one fruit per image).

Multi-fruits set size: 103 images (more than one fruit (or fruit class) per image)

Number of classes: 103 (fruits).

Image size: 100x100 pixels.

Filename format: image_index_100.jpg (e.g. 32_100.jpg) or r_image_index_100.jpg (e.g. r_32_100.jpg) or r2_image_index_100.jpg or r3_image_index_100.jpg. "r" stands for rotated fruit. "r2" means that the fruit was rotated around the 3rd axis. "100" comes from image size (100x100 pixels).

Different varieties of the same fruit (apple for instance) are stored as belonging to different classes.

## Download dataset
`kaggle datasets download -d moltean/fruits`

http://bit.ly/mdc-fruits360

https://www.kaggle.com/moltean/fruits


# Landmark Recognition
(Marcio)
Eu conversei um pouco com o Rafael sobre o projeto avançado. Segue resumo do que foi conversado.


1. temos 500 arquivos tar com imagens para treino. cada arquivo tar tem 1GB totalizando 500GB de imagens para treino. total de imagens para treino 4.132.914
2. cada arquivo .tar traz uma série de diretórios.
3. cada diretório tem mais de uma classe de imagens.
4. O arquivo train.csv tem a lista de todas as imagens e suas respectivas classes.
5. as classes são números e não textos.
6. importei o arquivo train.csv para um pandas dataframe. analisando o arquivo train.csv, identifiquei 203.094 classes distintas "len(df.landmark_id.unique())"
7. entre estas 203.094 classes, fica a nosso critério selecionar a quantidade de classes (recomendado 150 classes) bem como a quantidade de imagens por classe. priorizar as classes que tem mais imagens.
8. temos que segregar as imagens selecionadas entre treino, validação
9. temos 20 arquivos tar com imagens para teste. cada arquivo tar tem 500MB totalizando 10GB de imagens para teste. total de imagens para teste 117.577
10. temos que montar um diretório para cada classe selecionada. as imagens ficarão agrupadas nesses diretórios.
11. treinar um modelo que seja capaz de classificar a imagem corretamente. podemos fazer também clusterização.

O site abaixo detalha bem o dataset deste projeto.
https://github.com/cvdfoundation/google-landmark


Tem um outro conjunto de dados mais enxuto 52GB que podemos utilizar para estrutura a solução...mas este conjunto não pode ser utilizado no trabalho final. ele serve apenas para entendermos os dados.
https://www.kaggle.com/c/landmark-recognition-2019/discussion/91770#latest-537550

O link para fazer o donwload do arquivo tar de 52GB é esse.
https://drive.google.com/uc?id=10yVowvmFjMkY21-DGF2pej_Lbecfqou7