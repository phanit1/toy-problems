function countBs(str)
{
    var letter_Count = 0;
    for (var position = 0; position < str.length; position++) 
    {
        if (str.charAt(position) == 'B') 
        {
            letter_Count += 1;
        }
    }
    return letter_Count;
}
console.log("Count of Bs is ",countBs('Ballons should be blown'))
