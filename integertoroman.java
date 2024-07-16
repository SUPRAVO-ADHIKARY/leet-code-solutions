public class integertoroman {
    public static String integerToRoman(int num){
        String roman="";
        int romanValues[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] romanLetters= {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        for(int i=0;i<romanValues.length;i++){
            while (num>=romanValues[i]){
                roman=roman + romanLetters[i];
                num=num-romanValues[i];
            }
        }
        return roman;
    }

    public static void main(String[] args) {
        int num = 17;
        String result=integerToRoman(num);
        System.out.println(result);
    }
}
