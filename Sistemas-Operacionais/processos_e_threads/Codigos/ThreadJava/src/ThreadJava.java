import java.lang.Thread;
import java.lang.Math;

public class ThreadJava {
  public static void main(String[] args) throws Exception {

    ProcessThread thread1 = new ProcessThread(0, (int) (Math.random() * 5000));
    ProcessThread thread2 = new ProcessThread(1, (int) (Math.random() * 5000));
    ProcessThread thread3 = new ProcessThread(2, (int) (Math.random() * 5000));

    thread1.start();
    thread2.start();
    thread3.start();

  }
}
