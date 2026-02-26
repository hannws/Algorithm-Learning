import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main{
     public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();

        BigInteger x1 = new BigInteger(br.readLine());
        BigInteger x2 = new BigInteger(br.readLine());
        
        System.out.println(x1.multiply(x2));
    }
}