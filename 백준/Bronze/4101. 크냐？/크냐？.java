import java.util.*;
import java.io.*;

public class Main{
     public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (x == 0 && y == 0)
                break;
            sb.append(x>y ? "Yes" : "No").append('\n');
        }
        System.out.print(sb);
    }
}