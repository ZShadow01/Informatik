package com.company;

import java.util.Scanner;

public class Main {

    static String benutzername = "Wilhelm";
    static String kennwort = "Raabe";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Benutzername: ");
        String username = scanner.nextLine();

        System.out.print("Kennwort: ");
        String passwort = scanner.nextLine();

        if (username.equals(benutzername) && kennwort.equals(kennwort)) {
            System.out.println("Richtig");
        } else {
            System.out.println("Falsch");
        }
    }
}
