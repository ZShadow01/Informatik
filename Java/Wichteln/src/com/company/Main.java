package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Main {
    public static String fileName = "wichteln.txt";
    public static String resultFile = "wichteln_ergebnis.txt";

    public static HashMap<Character, HashMap<String, List<String>>> DATA = new HashMap<>();
    public static List<Integer> presents = new ArrayList<>();

    public static int amountOfStudents;

    public static String[] openFile() {
        List<String> lines = new ArrayList<>();

        File data = new File(fileName);

        try {
            Scanner reader = new Scanner(data);

            while (reader.hasNextLine()) {
                String line = reader.nextLine().trim();

                lines.add(line);
            }

            reader.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }

        return lines.toArray(new String[lines.size()]);
    }

    public static void updateData() {
        String[] data = openFile();

        amountOfStudents = Integer.parseInt(data[0]);

        String[] newData = new String[data.length - 1];
        for (int i = 0, j = 0; i < data.length; i++) {
            if (i != 0) {
                newData[j++] = data[i];
            }
        }

        for (int i = 1; i < amountOfStudents + 1; i++) presents.add(i);

        for (int i = 0, j = 1; i < newData.length; i++) {
            String line = newData[i];

            String[] newLine = line.trim().split(" +");

            int REDIX = 10;
            char studentChar = Character.forDigit(i, REDIX);
            DATA.put(studentChar, new HashMap<>());
            DATA.get(studentChar).put("WISHES", Arrays.asList(newLine));
            DATA.get(studentChar).put("RECEIVED", Arrays.asList(new String[1]));
        }
    }

    public static void give(char student, int rankedWish) {
        int present;

        if (rankedWish >= 3) {
            present = new Random().nextInt(presents.size());
        } else {
            present = presents.indexOf(Integer.parseInt(DATA.get(student).get("WISHES").get(rankedWish)));
        }

        DATA.get(student).get("RECEIVED").set(0, presents.remove(present).toString());
    }

    public static void sort() {
        for (int student = 0; student < DATA.size(); student++) {
            int REDIX = 10;
            char studentChar = Character.forDigit(student, REDIX);

            if (DATA.get(studentChar).get("RECEIVED").get(0) == null) {
                List<String> studentData = DATA.get(studentChar).get("WISHES");

                if (presents.contains(Integer.parseInt(studentData.get(0)))) {
                    give(studentChar, 0);
                } else if (presents.contains(Integer.parseInt(studentData.get(1)))) {
                    give(studentChar, 1);
                } else if (presents.contains(Integer.parseInt(studentData.get(2)))) {
                    give(studentChar, 2);
                } else {
                    give(studentChar, 3);
                }
            }
        }
    }

    public static void saveFile() throws IOException {
        File result = new File(resultFile);

        try {
            if (!result.exists()) {
                result.createNewFile();
            }

            FileWriter writer = new FileWriter(resultFile);
            for (int student = 0; student < DATA.size(); student++) {
                char studentChar = Character.forDigit(student, 10);
                int studentNumber = student + 1;
                String studentPresent = DATA.get(studentChar).get("RECEIVED").get(0);
                List<String> studentWishes = DATA.get(studentChar).get("WISHES");

                writer.write("Student " + studentNumber + " kriegt Geschenk Nr. " + studentPresent + " || Wunschliste: " + studentWishes + "\n");
            }
            writer.close();
        }
        catch (IOException e) {
            System.out.println("An error occured");
            e.printStackTrace();
        }
    }

    public static void run() throws IOException {
        System.out.println("[UPDATING]...");
        updateData();
        System.out.println("Done...");

        System.out.println("[SORTING]...");
        sort();
        System.out.println("Done...");

        System.out.println("[SAVING]...");
        saveFile();
        System.out.println("Done...");
    }

    public static void main(String[] args) throws IOException {
        run();
    }
}
