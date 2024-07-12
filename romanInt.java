public class romanInt {
    public static int position(char a){
        char roman[]={'I','V','X','L','C','D','M'};
        int answer=-1;
        for (int i=0;i<7;i++){
            if(a==roman[i]){
                answer=i;
            }
        }
        return  answer;
    }
    public static int romanToInt(String s){
        s=s.toUpperCase();
        int values[]={1,5,10,50,100,500,1000};
        int result=0;
        int l = s.length();
        int c1,c2;
        for (int i =0;i<l;i++){
            c1=position(s.charAt(i));
            if(i!=l-1){
                c2=position(s.charAt(i+1));
                if(c1<c2){
                    result=result+(values[c2]-values[c1]);
                    i=i+1;
                    continue;
                }
                else {
                    result=result+values[c1];
                }
            }
            else {
                result=result+values[c1];
            }
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.print(romanToInt("MCx"));
    }
}
