import java.util.Scanner;

public class Main{
     public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.nextInt();
        for (int i = 0; i < x; i++){
            sc.nextInt();
            sc.nextInt();
        }

        System.out.println("비와이");

        sc.close();
    }
}