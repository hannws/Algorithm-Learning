import java.util.*;
import java.io.*;

public class Main{
     public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        if(x<y || (x+y) % 2 != 0){
            System.out.print(-1);
            return;
        }

        int a, b;
        a = (x+y)/2;
        b = (x-y)/2;
        System.out.println(a+" "+b);
    }
}