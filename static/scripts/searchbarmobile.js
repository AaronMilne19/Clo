





function checkMatching( listOfWordsToCheck, inputText ){

    for(i = 0; i < listOfWordsToCheck.length; i++ ){
        if (listOfWordsToCheck[0].toUpperCase().indexOf(inputText) > -1 ){
            return true;
        }
    }
    return false;

}