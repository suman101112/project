#This should contain the commands to run your programs
#For Java, this should contain 'java program_name input_file'
#For Python, this file should contain 'python program_name.py input_file'
#The output of the program should be displayed on the terminal
#This file should not be left blank

cd ../src/

echo "tokenizing the marathi data"
echo "padding the sentences of marathi and calculating all the uni,bi,tri and 5-grams"
echo "& calculating feature values for all the trigrams" 
python PMI_Dict.py
echo "*************** writing all outputs to the files <marathi_100sentences_tokenized.txt>"
echo "<marathi_100sentences_uni_grams.txt>"
echo "<marathi_100sentences_bi_grams.txt>"
echo "<marathi_100sentences_tri_grams.txt>"
echo "<marathi_100sentences_five_grams.txt>"
echo "<marathi_100sentencesP.txt>"
echo "<marathi_100sentences_Tris.txt>"
echo ""
echo "calculating all the similarities between each and every two trigrams"
python Trig_Sim_Dict.py
echo "*************** writing all outputs to the files <marathi_100sentences_Simlr.txt>"
echo ""
python NbrCount.py
echo "*************** writing all outputs to the files <marathi_100sentences_Nbr.txt> <marathi_100sentences_5Nbr.txt> <marathi_100sentences_Centers.txt>"
echo ""
python RIs_QIs.py
echo "*************** writing all outputs to the files <marathi_100sentences_QI's.txt>"
echo ""
echo "Reading all Qi s values... & getting most probable tags"
echo "Assigning Tags to target language sentences"
python Tagg.py
echo "TAGGED OUTPUT IS IN THE RESULTS FOLDER"
