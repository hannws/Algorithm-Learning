import java.util.*;
import java.io.*;

public class Main{
     public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        for (int i = 0; i<4; i++){
            int t1 = Integer.parseInt(br.readLine());
            result += t1;
        }
        System.out.print(result/60 + "\n" + result%60);
    }
}