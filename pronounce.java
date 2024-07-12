public class pronounce {
    public static boolean easyPronounces(String s){
        boolean flag=false;
        s=s.toLowerCase();
        int count=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='a' || s.charAt(i)=='e' || s.charAt(i)=='i' || s.charAt(i)=='o' || s.charAt(i)=='u'){
                count+=1;
                if(count==4){
                    flag=true;
                    return flag;
                }
            }
            else {
                count=0;
            }
        }
        return flag;
    }

    public static void main(String[] args) {
        String s="aswaeiounmjk";
        boolean c;
        c=easyPronounces(s);
        if(c==true){
            System.out.println("easy to pronounce");
        }
        else {
            System.out.println("not easy to pronounce");
        }
    }
}
