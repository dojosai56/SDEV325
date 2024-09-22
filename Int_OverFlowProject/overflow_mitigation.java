/**
 * Class overflow_mitigation
 */
public class overflow_mitigation {
	public static void main(String[] args) {
    	int value = Integer.MAX_VALUE-1;
        for(int counter = 0; counter < 5; counter++) {
        System.out.println(value);
        value = Math.addExact(value, 1);
}
	}
}