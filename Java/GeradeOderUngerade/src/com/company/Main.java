package com.company;

public class Main {

    static int[] numbers = new int[] { 2, 5, 12, 13, 27, 154, 634 };

    public static void main(String[] args) {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                System.out.println(numbers[i] + " ist gerade");
            } else {
                System.out.println(numbers[i] + " ist ungerade");
            }
        }
    }
}
