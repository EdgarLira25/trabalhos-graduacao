public class ProcessThread extends Thread {

  int id;
  int tempo;

  public ProcessThread(int id, int tempo) {
    this.id = id;
    this.tempo = tempo;
  }

  public void run() {

    try {

      System.out.println("ID = " + id + " vai dormir por " + tempo + ("ms"));

      Thread.sleep(tempo);

      System.out.println("Hello World, ID = " + id);

    } catch (InterruptedException e) {

      e.printStackTrace();

    }
  }
}
