import java.util.ArrayList;
import java.util.List;
import java.util.Collections;


public class Solution {
	public static void main(String[] args) {
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		solution(array, commands);
	}
	public static int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        ArrayList<Integer> result = new ArrayList<Integer>();
        ArrayList<Integer> result2 = new ArrayList<Integer>();
        
        
        for(int x=0;x<commands.length;x++) {
        	for(int i : array) result.add(i);
        	System.out.println("result : "+result);
        	System.out.println(commands[x][0]+" , " + commands[x][1]);
        	List<Integer> result1 = new ArrayList<Integer>(result.subList(commands[x][0], commands[x][1]));
            
            Collections.sort(result1);
            System.out.println("result1 : "+result1);
            
            
            int z = commands[x][2]-1;
            System.out.println("z : "+z);
            result2.add(result1.get(result1.indexOf(z)));
            
            System.out.println("result2 :"+result2);
            result.clear();
            result1.removeAll(result);
//            result1.subList().clear();
            
        }
        
        
        
        
        return answer;
    }
}
