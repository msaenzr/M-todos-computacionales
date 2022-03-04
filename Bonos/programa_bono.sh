cd "Actividad 2 Descargar 11 de febrero de 2022 1200"
IFS='
'
for i in $(ls)
do
echo -e "\nNOMBRE CARPETA\n"
echo $i
cd $i
for j in $(ls)
do
echo -e "\nNOMBRE ARCHIVO PYTHON\n"
echo $j
echo e- "\nRESULTADO DEL PROGRAMA\n"
python $j
done
cd ../
done
cd ../
