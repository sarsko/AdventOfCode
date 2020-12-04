import java.util.*;
public class day03{
    public static void main(String[] args){
        int lon = 3;
        int crashes = 0;
        int decCounter = 0;
        int right = 0;
        char loc;
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        for (int i = 0; i < 322; i++){
            line = sc.nextLine();
            right = right+lon;
            while (true){
                try {
                    loc = line.charAt(right-decCounter);
                    if (decCounter > 0){
                        loc = line.charAt(decCounter-1);
                    }
                    System.out.println(loc);
                    if (loc == '#'){
                        crashes++;
                    }
                    if (decCounter > 0){
                        right = decCounter-1;
                    }
                    decCounter = 0;
                    break;
                }
                catch (Exception e){
                    decCounter++;
                }
            }

        }
        System.out.println(crashes);
    }
}
