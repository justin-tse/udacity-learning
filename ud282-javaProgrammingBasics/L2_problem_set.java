int passcode = 555;
String coffeeType;
switch (passcode) {
  case 555: coffeeType = "Espresso";
      break;
  case 312: coffeeType = "Vanilla latte";
      break;
  case 629: coffeeType = "Drip coffee";
      break;
  default : coffeeType = "Unknown";
      break;
}
System.out.println("coffeeType");

if (canSeePlayer) {
  if (!playerPoweredUp) {
      System.out.println("Attack!");
  } else {
      System.out.println("Run away!");
  }
} else {
    System.out.println("Wander.");
}