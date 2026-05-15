public class Armstrong {

  static boolean armstrong(int n){
    int arm = 0;
    int num = n;
    while(n>0){
      arm = arm + Math.pow(n%10,3);
      n = n / 10;
    }
    return arm == num;
  }
  public static void main(String[] args) {
    System.out.println(armstrong(120));
  }
}
