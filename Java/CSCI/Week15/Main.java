
public class Main {

  public static void main(String[] args) {
    System.out.println("Program starting...");

    Elf ann = new Elf("Ann", 22);
    ann.introduceSelf();

    Orc throg = new Orc("Throg", 33, "The Evil Ones");
    throg.introduceSelf();

    Hobgoblin gorvash = new Hobgoblin("Gorvash", 76, "The Fangbreakers");
    gorvash.introduceSelf();

    HalfElf gengar = new HalfElf("Gengar", 89);
    gengar.introduceSelf();

    ann.attacks(gorvash);
    gorvash.attacks(ann);
    throg.attacks(ann);
    gengar.attacks(throg);

  }
}

class Person {
  protected String name;
  protected int lifePoints;
  protected boolean isAlive;

  public Person (String userName, int userLifePoints) {
    name = userName;
    lifePoints = userLifePoints;
    if (lifePoints > 0) {
      isAlive = true;
    } else {
      isAlive = false;
    }
  }

  public void introduceSelf() {
    System.out.println("Hi, I'm " + name);
  }

  public String getName() {
    return name;
  }

  public boolean isAlive() {
    return isAlive;
  }

  public void attacks(Person userPerson) {
    if (this.isAlive() && userPerson.isAlive()) {
      System.out.println(this.getName()+" attacks "+userPerson.getName());
      userPerson.isHit(50);
    }
  }

  public void isHit(int x) {
    lifePoints = lifePoints - x;
    if (lifePoints < 1) {
      isAlive = false;
      System.out.println(name+" falls!");
    }
  }
}

class Elf extends Person {
  public Elf (String userName, int userLifePoints) {
    super(userName, userLifePoints);
  }

  @Override
  public void attacks(Person userPerson) {
    if (this.isAlive() && userPerson.isAlive()) {
      System.out.println(this.getName()+" shoots "+userPerson.getName());
      userPerson.isHit(50);
    }
  }

  @Override
  public void introduceSelf() {
    super.introduceSelf();
  }
}

class HalfElf extends Elf{
  protected int lifePoints;
  protected String familyName;
  protected String name;
  public HalfElf (String userName, int userLifePoints){
    super(userName, userLifePoints);
    lifePoints = userLifePoints;
    name = userName;
    
  }

  @Override
  public void introduceSelf(){
    super.introduceSelf();
    
  }

  @Override
  public void attacks(Person userPerson ){
    if (this.isAlive() && userPerson.isAlive()) {
      System.out.println(this.getName() + " uses Shadow Ball on " + userPerson.getName());
      userPerson.isHit(50);
    }
  }
}

class Orc extends Person {
  protected String tribe;
  
  public Orc(String userName, int userLifePoints, String userTribe) {
    super(userName, userLifePoints);
    tribe = userTribe;
  }

  @Override
  public void introduceSelf() {
    System.out.println("Arr, I'm " + name + " of the tribe " + tribe);
  }

  @Override
  public void attacks(Person userPerson) {
    if (this.isAlive() && userPerson.isAlive()) {
      System.out.println(this.getName()+" charges "+userPerson.getName());
      userPerson.isHit(50);
    }
  }
}

class Hobgoblin extends Orc {
  public Hobgoblin(String userName, int userLifePoints, String userTribe) {
    super(userName, userLifePoints, userTribe);
  }
}