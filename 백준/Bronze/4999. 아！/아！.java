import java.util.*;
import java.io.*;

public class Main{
     public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String x = br.readLine();
        String y = br.readLine();

        System.out.println(x.length() >= y.length() ? "go" : "no");
    }
}