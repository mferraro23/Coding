import java.util.Scanner;

class Human {
  public String name;
  private int hp;
  public boolean alive;

  public Human(String x, int y) {
    this.name = x;
    this.hp = y;
    alive = true;
  }

  public void isHit(int x) {
    this.hp = this.hp - x;
    System.out.println("Human's Health: " + this.hp);
    if (hp <= 0) {
      this.alive = false;
      System.out.println(this.name+" falls!");
    }
  }

  public void attackOrc(Orc orc) {
    System.out.println(this.name + " says 'die orc!!'");
    orc.isHit(4);
  }

  public void heal(int x){
    this.hp = this.hp + x;
    System.out.println("Human's Health: " + this.hp);
  }
}

class Orc {
  public String name;
  private int hp;
  public boolean alive;

  public Orc(String x, int y) {
    name = x;
    hp = y;
    this.alive = true;
  }

  public void isHit(int x) {
    this.hp = this.hp - x;
    System.out.println("Orc's Health: " + this.hp);
    if (hp <= 0) {
      this.alive = false;
      System.out.println(this.name+" falls!");
    }
  }

  public void crushHuman(Human human) {
    System.out.println(this.name+ " cries out for blood!!!");
    human.isHit(5);
  }
  public void heal(int x){
    this.hp = this.hp + x;
    System.out.println("Orc's Health: " + this.hp);
  }
}

class Healer{
  public String name;
  private int hp;
  public boolean alive;
  public String target;

  public Healer(String x, int y){
    name = x;
    hp = y;
    this.alive = true;
  }
  
  public void takeDamageFromHealing (String target){ //replaces isHit
    if (this.hp>0){
      this.hp = this.hp - 25;
      System.out.println("Healer takes self damage due to healing!");
      System.out.println("Healer's Health: " + this.hp);
    }
    if (this.hp<=0){
      this.alive = false;
      System.out.println(this.name + " falls and can no longer heal " + target);
    }
  }

  public void helpTarget(String targetName, Human human, Orc orc){
    target = targetName;
    if (target.equalsIgnoreCase("human")){
      System.out.println(this.name + " heals " + target + " by 5 hit points!");
      human.heal(5);
      takeDamageFromHealing(target);
    }
    else if (target.equalsIgnoreCase("orc")){
      System.out.println(this.name + " heals " + target + " by 5 hit points!");
      orc.heal(5);
      takeDamageFromHealing(target);
    }

  }
}
class Main_HW {
  public static void main(String[] args) {
    System.out.println("Program running");
    Scanner scnr = new Scanner(System.in);
    String name;
    int hp;
    String partner;

    System.out.println("Enter healer name: ");
    name = scnr.nextLine();
    System.out.println("Enter healer hp: ");
    hp = scnr.nextInt();
    System.out.println("Enter parter name (human or orc): ");
    scnr.nextLine();
    partner = scnr.nextLine();
    Healer healer = new Healer(name, hp);
    
    System.out.println("Enter human name: ");
    name = scnr.nextLine();
    System.out.println("Enter human hp: ");
    hp = scnr.nextInt();

    Human human = new Human(name, hp);
  
    scnr.nextLine();

    System.out.println("Enter orc name: ");
    name = scnr.nextLine();
    System.out.println("Enter orc hp: ");
    hp = scnr.nextInt();
    Orc orc = new Orc(name, hp);

    scnr.nextLine();

    while (human.alive && orc.alive) {
      fight(human, orc, healer, partner);
    }

    if (human.alive) {
      System.out.println(human.name+" survives...");
    }
    if (orc.alive) {
      System.out.println(orc.name+" survives...");
    }

    scnr.close();
  }

  public static void fight(Human x, Orc y, Healer j, String f) {
    x.attackOrc(y);
    y.crushHuman(x);
    if (j.alive){
      j.helpTarget(f, x, y);
    }
    else{
      System.out.println("Healer can no longer heal!");
    }
  }
}